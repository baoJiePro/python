var1 = 13
var2 = 99.99
var3 = True
var3_1 = False
var4 = 4 + 1j
var5 = "123321"
var6 = "你好123"

res = int(var2)
print(res)

# True 强转整型是1 False 强转整型是0
res = int(var3)
res = int(var3_1)
print(res)

res = int(var5)
print(res, type(res))

"""  *****五颗星 *****
布尔类型为假的十种情况:
0,0.0,False,0j,"",[],(),set(),{},None
None 是系统的一个关键字 表示空的,什么也没有,一般做初始值
"""
res = None
print(res, type(res))
