"""保留原始复现缓存，只从训练索引剔除审计命中的测试题，不改验证集。"""

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / 'src'))

import json
import shutil
from pathlib import Path
from c2c.c2c_prepare_formal_data import digest, write

from project_paths import asset_dir
from argparse import ArgumentParser
parser = ArgumentParser(description='从训练划分中排除与测试题重合的三行。')
parser.add_argument('--root', type=Path, default=Path.cwd())
root=parser.parse_args().root.resolve()
source=asset_dir(root,'data')/'openhermes_formal_b82037821055'
target=asset_dir(root,'data')/'openhermes_clean_b82037821055'
target.mkdir(exist_ok=False)

rows=json.loads((source/'source_rows.json').read_text())
split=json.loads((source/'split.json').read_text())
bad={117050, 118479, 118480}
kept=[(idx,row) for idx,row in zip(split['train_indices'],rows['train']) if row not in bad]
split['train_indices']=[i for i,_ in kept]
write(target/'split.json',split)
write(target/'source_rows.json',{'train':[r for _,r in kept],'validation':rows['validation']})
# 同机缓存仅硬链接已有普通文件，数据内容不复制或修改。
shutil.copytree(source/'filtered',target/'filtered',copy_function=__import__('os').link)
manifest=json.loads((source/'manifest.json').read_text())
manifest.update(train_rows=len(kept),split_sha256=digest(target/'split.json'),source_rows_sha256=digest(target/'source_rows.json'),
                cache=str(target/'filtered'),test_overlap='固定题目完整文本重合核查完成，训练索引剔除命中3行；模糊改写未检验',
                original_manifest_sha256=digest(source/'manifest.json'),removed_source_rows=sorted(bad),
                preprocessing_difference='原前500K/2048过滤不变；99/1划分后只剔除训练中3条GSM8K测试重合记录，验证不变',
                effective_train_ratio=len(kept)/(len(kept)+manifest['validation_rows']),clean_code_sha256=digest(__file__))
write(target/'manifest.json',manifest)

print(json.dumps(manifest,ensure_ascii=False),flush=True)
