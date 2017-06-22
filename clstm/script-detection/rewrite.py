#! /usr/bin/env python
# maps into PUA-A

import re
import os
import glob
import sys
import json
import shutil

idx = 0

blocks = json.load(open('blocks.json', 'r'))

t = set()

def block(ch):
    assert isinstance(ch, unicode) and len(ch) == 1, repr(ch)
    cp = ord(ch)
    for id, start, end, name in blocks:
        if start <= cp <= end:
            t.add(name)
            return unichr(id)

for f in glob.glob(sys.argv[1] + '/*.gt.txt.d'):
    with open(f, mode='rb') as fp:
        with open(f[:-2], mode='wb') as fo:
            s = fp.read().decode('utf-8')
            fo.write(u''.join(block(c) for c in s).encode('utf-8'))

print(t)
