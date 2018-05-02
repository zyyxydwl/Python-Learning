#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

jsondata='{"a":1,"b":2,"c":3}'
with open('a.txt','w') as f:
    json.dump(jsondata,f)

with open('a.txt','r') as fr:
    m=json.load(fr)
    print(m)


