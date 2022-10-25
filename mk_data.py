#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/25 

# 更新音频片段数据库 static/data/main/main.json
# 用 Hana 声源替换 Miku

import os
import json
from random import choices, sample, shuffle
import base64

DB_FILE = 'static/data/main/main.json'
MP3_PATH = 'mp3'


def encode_mp3(mp3_fp):
  prefix = 'data:audio/mp3;base64,'
  
  with open(mp3_fp, 'rb') as fh:
    bdata = fh.read().strip()
  out = base64.b64encode(bdata)

  return prefix + out.decode()


def make_hana():
  with open(DB_FILE, 'r', encoding='utf-8') as fh:
    db = json.load(fh)
    len_db = len(db)

  mp3_fns = [fn for fn in os.listdir(MP3_PATH) if fn.lower().endswith('mp3')]
  len_mp3 = len(mp3_fns)

  if len_mp3 == len_db:
    print(f'>> found {len_mp3} available sound clips, need {len_db} sound clips, just perfectly match!')
  elif len_mp3 > len_db:
    print(f'>> found {len_mp3} available sound clips, need {len_db} sound clips, random picking a subset')
    mp3_fns = sample(mp3_fns, len_db)
  elif len_mp3 < len_db:
    print(f'>> found {len_mp3} available sound clips, need {len_db} sound clips, repeating some clips')
    mp3_fns = choices(mp3_fns, len_db)
  
  shuffle(mp3_fns)
  len_mp3 = len(mp3_fns)
  assert len_mp3 == len_db

  keys = sorted(db.keys())
  for i, k in enumerate(keys):
    db[k] = encode_mp3(os.path.join(MP3_PATH, mp3_fns[i]))

  with open(DB_FILE, 'w', encoding='utf-8') as fh:
    json.dump(db, fh, indent=2)

  print(f'>> write db file {DB_FILE}')


if __name__ == '__main__':
  make_hana()
