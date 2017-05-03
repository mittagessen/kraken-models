#! /usr/bin/env python

import os
import sys
import json
import clstm
import shutil

from kraken.lib.models import load_clstm

rnn = load_clstm(sys.argv[1])

alphabet = []
cls = clstm.Classes()
cls.resize(1)
for i in range(1, rnn.rnn.noutput()):
    cls[0] = i
    alphabet.append(rnn.rnn.decode(cls))

s = {}
s['summary'] = raw_input('summary: ')
s['description'] = raw_input('description: ')
s['author'] = raw_input('author: ')
s['author-email'] = raw_input('author-email: ')
s['license'] = raw_input('license: ')
s['url'] = raw_input('url: ')
s['script'] = raw_input('scripts (split by whitespace): ').split(' ')
s['graphemes'] = alphabet
s['name'] = os.path.basename(sys.argv[1])

odir = os.path.splitext(os.path.basename(sys.argv[1]))[0]
try: 
    os.mkdir(odir)
except:
    pass

with open(os.path.join(odir, 'DESCRIPTION'), 'wb') as fp:
    json.dump(s, fp, sort_keys=True, indent=4, separators=(',', ': '))

shutil.copyfile(sys.argv[1], os.path.join(odir, os.path.basename(sys.argv[1])))
