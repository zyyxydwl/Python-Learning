#!/usr/bin/env python
# -*- coding:utf-8 -*-

from io import BytesIO
f = BytesIO()
f.write('向往'.encode('utf-8'))

print(f.getvalue())

# 运行结果
# b'\xe5\x90\x91\xe5\xbe\x80'
# 运行结果




from io import BytesIO
f = BytesIO(b'\xe5\x90\x91\xe5\xbe\x80')
f.read()

# 运行结果
# b'\xe5\x90\x91\xe5\xbe\x80'
# 运行结果

