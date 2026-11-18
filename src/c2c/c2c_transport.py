"""完整KV无损序列化与本机回环传输诊断。"""

import io
import queue
import socket
import struct
import threading


def serialize_kv(keys, values, metadata):
    """元数据与完整K/V一起编码，计量真正发送的应用层载荷。"""
    import torch
    buffer = io.BytesIO()
    torch.save({'schema_version':1,'metadata':metadata,'keys':keys,'values':values},buffer)
    return buffer.getvalue()


def deserialize_kv(payload):
    """仅加载本轮自产张量与普通字段，接收后保留原dtype和形状。"""
    import torch
    value = torch.load(io.BytesIO(payload),map_location='cpu',weights_only=True)
    if value['schema_version'] != 1 or len(value['keys']) != len(value['values']):
        raise ValueError('KV消息版本或层数不匹配')
    return value


class LoopbackChannel:
    """单向TCP发送并在接收线程收齐；不通过回显额外发送第二份KV。"""

    def __init__(self, io_timeout=30):
        self.io_timeout = io_timeout
        listener = socket.socket()
        listener.bind(('127.0.0.1',0));listener.listen(1)
        self.client = socket.create_connection(listener.getsockname(),timeout=io_timeout)
        self.server,_ = listener.accept();listener.close()
        self.server.settimeout(io_timeout)
        self.messages = queue.Queue(maxsize=1)
        self.closed = False
        self.reader = threading.Thread(target=self._receive,daemon=True)
        self.reader.start()

    def _read_exact(self, size):
        result = bytearray(size)
        view = memoryview(result)
        position = 0
        while position < size:
            count = self.server.recv_into(view[position:])
            if not count:
                raise EOFError('连接在载荷接收完毕前结束')
            position += count
        return bytes(result)

    def _receive(self):
        while not self.closed:
            try:
                # 两题之间可能长时间解码；只有消息开始后才启用传输超时。
                self.server.settimeout(None)
                first = self.server.recv(1)
                if not first:
                    raise EOFError('连接已关闭')
                self.server.settimeout(self.io_timeout)
                header = first + self._read_exact(7)
                size = struct.unpack('!Q',header)[0]
                self.messages.put((self._read_exact(size),size+len(header)))
            except Exception as error:
                if not self.closed:
                    self.messages.put(error)
                return

    def transfer(self, payload):
        """记录接收端实际收齐的字节，口径不含TCP/IP包头。"""
        self.client.sendall(struct.pack('!Q',len(payload)))
        self.client.sendall(payload)
        received = self.messages.get(timeout=self.io_timeout)
        if isinstance(received,Exception):
            raise received
        content,count = received
        if count != len(payload)+8 or content != payload:
            raise ValueError('载荷内容或实际接收长度不符')
        return content,count

    def close(self):
        self.closed = True
        # 唤醒正在等待下一条消息的接收线程。
        for connection in (self.client, self.server):
            try:
                connection.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
        self.client.close();self.server.close()
        self.reader.join(timeout=1)

    def __enter__(self):
        return self

    def __exit__(self,*_):
        self.close()
