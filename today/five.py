# str 强转成字符串类型
# ( 容器类型数据  /  Number类型数据 都可以 )
var1 = "快乐每一天"
var2 = [1, 2, 3]
var3 = (4, 5, 6)
var4 = {"美丽", "店铺名个人"}
var5 = {"a": 1, "b": 2, "c": 3}
var6 = 123

res = str(var2)
res = str(var3)
res = str(var5)
print(repr(res), type(res))

# list  列表强转规律:
'''
如果是字符串:把字符串中的每一个字符当成新的元素放到列表中
如果是其他数据:就是单纯的把原标识符换成[]
'''

res = list(var1)
print(res)

# tuple 元组强转规律
"""
如果是字符串:把字符串中的每一个字符当成新的元素放到元组中
如果是其他数据:就是单纯的把原标识符换成() 变成元组即可
"""
res = tuple(var1)
res = tuple(var2)
res = tuple(var5)  # 强转字典时,保留键,舍去值
print(res)

# set 集合强转规律
"""
如果是字符串:把字符串中的每一个字符当成新的元素放到集合中
如果是其他数据:就是单纯的把原标识符换成{} 变成集合即可
"""
res = set(var1)  # 因为无序,字符串被打散
res = set(var2)  # {1,2,3}
res = set(var5)  # 强转字典时,保留键,舍去值,键值顺序被打乱
print(res)

# 过滤列表重复数据
listvar = [2, 1, 3, 4, 5, 5, 6, 7, 6]
container = set(listvar)
print(container)
container = list(container)
print(container, type(container))

tuplevar = (["c", 11], ("d", 23))  # 推荐 ***
res = dict(tuplevar)
print(res)


