"""将停机请求延后到完整更新边界，供同一正式计划跨窗口接续。"""

import signal
import json
import os
import time
from pathlib import Path


class BoundaryStop:
    """接受STOP_REQUEST文件或TERM/INT信号，训练循环负责保存后退出。"""

    def __init__(self, request_file):
        self.request_file = Path(request_file)
        self.received_signal = None
        self.handlers = {}

    def __enter__(self):
        for name in (signal.SIGTERM, signal.SIGINT):
            self.handlers[name] = signal.getsignal(name)
            signal.signal(name, self._receive)
        return self

    def _receive(self, signum, frame):
        """信号处理器只置标记，保存操作由主循环执行。"""
        self.received_signal = signum

    def __call__(self):
        return self.received_signal is not None or self.request_file.exists()

    def __exit__(self, *args):
        for name, handler in self.handlers.items():
            signal.signal(name, handler)


class BoundaryCheckpoint:
    """更新边界内保存后继续运行；计时及请求不触碰模型或随机状态。"""

    def __init__(self, request_file, interval_seconds=3600, clock=time.monotonic):
        if interval_seconds <= 0:
            raise ValueError('进程内保存间隔必须为正数')
        self.request_file = Path(request_file)
        self.interval_seconds = interval_seconds
        self.clock = clock
        self.last_saved = clock()
        self.token = None
        self.reasons = []

    def __call__(self):
        try:
            self.token = self.request_file.read_text(encoding='utf-8')
        except FileNotFoundError:
            self.token = None
        self.reasons = []
        if self.clock() - self.last_saved >= self.interval_seconds:
            self.reasons.append('runtime_interval')
        if self.token is not None:
            self.reasons.append('save_request')
        return bool(self.reasons)

    def committed(self, checkpoint, step):
        """全部原定保存也重置计时；成功写入日志后才确认本次请求。"""
        self.last_saved = self.clock()
        receipt = {'step': step, 'checkpoint': str(checkpoint), 'saved_at': time.time(),
                   'pid': os.getpid(), 'reasons': list(self.reasons), 'request_token': self.token}
        destination = self.request_file.with_name('checkpoint_status.json')
        temporary = destination.with_suffix('.tmp')
        with temporary.open('w', encoding='utf-8') as stream:
            json.dump(receipt, stream, ensure_ascii=False, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(destination)
        # 控制器不覆盖已有请求；保留保存过程中出现的新请求。
        if self.token is not None:
            try:
                if self.request_file.read_text(encoding='utf-8') == self.token:
                    self.request_file.unlink()
            except FileNotFoundError:
                pass
        self.token = None
