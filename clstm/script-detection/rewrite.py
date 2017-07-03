#! /usr/bin/env python
# maps into PUA-A

import re
import os
import glob
import sys
import json
import shutil
import unicodedata

idx = 0

blocks = json.load(open('script.json', 'r'))

t = set()

def block(ch):
    assert isinstance(ch, unicode) and len(ch) == 1, repr(ch)
    cp = ord(ch)
    for start, end, name, id, _, _, _, _ in blocks:
        if cp == start or start <= cp <= end:
            t.add(name)
            return unichr(id + 0xF0000)
    return unichr(998 + 0xF0000)

for f in glob.glob(sys.argv[1] + '/*.gt.txt.d'):
    with open(f, mode='rb') as fp:
        with open(f[:-2], mode='wb') as fo:
            s = unicodedata.normalize('NFC', fp.read().decode('utf-8'))
            print(f)
            fo.write(u''.join(block(c) for c in s).encode('utf-8'))

print(t)
