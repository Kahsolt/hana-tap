#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/25 

# 长条语音自动切片到 mp3 目录

import os
import sys
from traceback import print_exc
import librosa as L
from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt

MP3_PATH = 'mp3'
WAV_FP   = 'tap.wav'
TMP_FILE = 'tmp.wav'

ENERGY_MIN = 0.05
LENGTH_MIN = 0.03  # ignore < 30ms

# load wav
if len(sys.argv) == 2: WAV_FP = sys.argv[1]
name, ext = os.path.splitext(os.path.basename(WAV_FP))
print(f'>> auto split file {WAV_FP!r}')

# detect segments
y, sr = L.load(WAV_FP, sr=None)
ref_db = y.max()
y = L.effects.trim(y=y, ref=ref_db)[0]

# interactive suppress breath & noise
clips = []
try:
  opt = None
  while opt != 'ok':
    # make a new copy
    wav = y.copy()
    
    # find segments
    onsets = L.onset.onset_detect(y=wav, sr=sr, units='samples', normalize=True)
    onsets_remove = []
    for i in range(len(onsets)-1):
      if onsets[i+1] - onsets[i] < sr * LENGTH_MIN:
        onsets_remove.append(onsets[i+1])
    onsets = sorted(set(onsets) - set(onsets_remove))

    # ignore silence
    clips.clear()
    onsets_ok = [ ]
    for i, (s, e) in enumerate(zip(onsets[:-1], onsets[1:])):
      clip = wav[s : e]
      trimed = L.effects.trim(y=clip, ref=ref_db)[0]

      if len(trimed) < sr * LENGTH_MIN:
        wav[s:e] = 0
        continue
      if L.feature.rms(trimed).mean() < ENERGY_MIN:
        wav[s:e] = 0
        continue

      onsets_ok.append(s)
      pre_offset = int(sr * LENGTH_MIN)
      clips.append(wav[max(0, s - pre_offset) : e])
    
    print(f'>> found {len(clips)} clips')

    # draw constrast
    plt.subplot(211) ; plt.plot(y, 'b')
    plt.subplot(212) ; plt.plot(wav, 'r') ; plt.vlines(onsets_ok, ymin=-0.5, ymax=0.5, color='grey', alpha=0.75, linestyle='--', label='Onsets')
    plt.suptitle(f'>> found {len(clips)} clips; tune E_min to suppress breath and noise to silence')
    plt.show()

    # ask for option
    while True:
      opt = input(f'输入 ok 保存，否则输入新的 E_min (当前: {ENERGY_MIN}): ').strip().lower()
      if opt == 'ok': break 
      try:
        ENERGY_MIN = float(opt)
        break
      except: pass
except Exception:
  print_exc()
  exit(-1)

# save clips
print(f'>> found {len(clips)} clips')
for i, clip in enumerate(clips):
  wavfile.write(TMP_FILE, sr, clip)
  seg = AudioSegment.from_wav(TMP_FILE)
  fp = os.path.join(MP3_PATH, f'{name}-{i}.mp3')
  print(f'>> saving {fp}')
  seg.export(fp, format='mp3')

# clean tmp file
if os.path.exists(TMP_FILE):
  os.unlink(TMP_FILE)
