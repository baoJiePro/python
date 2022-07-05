# 浅拷贝
# 方法一
listvar = [1, 2, 3, 4, 5]
lst2 = listvar.copy()
listvar.append(6)
print(lst2)

import copy

listvar = [1, 2, 3, 4, 5]
lst = copy.copy(listvar)
listvar.append(14)
print(lst)

# 深拷贝
import copy

lst = [
    {"a": {'c': 1, 'd': 3}, "b": [5, 6, 7, 8]},
    4, 5
]
# 浅拷贝只能拷贝列表的一级 , 如果想要拷贝所有层级,需要使用深拷贝
lst2 = copy.deepcopy(lst)
lst[0]['b'].append(9)
print(lst)
print(lst2)

# keys()   将字典的键组成新的可迭代对象
dictvar = {"top": "程咬金", "middle": "甄姬", "bottom": "鲁班七号"}
res = dictvar.keys()
print(res)
for i in dictvar.keys():
    print(i)

for i in dictvar:
    print(i)

# values() 将字典中的值组成新的可迭代对象
dictvar = {"top": "程咬金", "middle": "甄姬", "bottom": "鲁班七号"}
res = dictvar.values()
print(res)
for i in res:
    print(i)

# items()  将字典的键值对凑成一个个元组,组成新的可迭代对象
res = dictvar.items()
print(res)
for i in res:
    print(i)
'''
('top', '程咬金')
('middle', '甄姬')
('bottom', '鲁班七号')
'''
for a, b in res:
    print(a, b)
