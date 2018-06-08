#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/17 22:21
# @Author  : zhouyuyao
# @File    : demon2.py
#!/usr/bin/env python
import memcache

mc = memcache.Client(['120.78.254.132:22222'],debug=1)
# debug=1 表示运行出现错误时，可以显示错误信息

mc.set("some_key", "Some value")
value = mc.get("some_key")
print(value)

# 结果 Some value

mc.set('name','zyy')                  # 设置key
mc.set('name','zhouyuyao')            # 设置key,key存在则更新
print(mc.get('name'))

# 结果 zhouyuyao
mc.set('name1','zhouyuyao1')                 # 设置key,key存在则更新
mc.set('k1','zhouyuyao2')                 # 设置key,key存在则更新
mc.set_multi({'k1':'zhouyuyao3','k2':'v2'})          # 批量设置key

print(mc.get_multi(('k1','k2'),key_prefix=''))       # 批量获取key
print(mc.get_multi(['k1','k2']))                 # 批量获取key

mc.delete("another_key")

mc.replace("key", "1")   # note that the key used for incr/decr must be a string.
mc.set('age','22')
print(mc.incr("age" ,delta=2))
print(mc.decr("age" ,delta=2))
# incr(self, key, delta=1, noreply=False)
mc.decr("key")
