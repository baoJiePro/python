# ### 集合的相关操作 作用:交差并补
set1 = {"周星驰", "周杰伦", "周润发", "王文"}
set2 = {"王健林", "王思聪", "王宝强", "王文"}
# intersection() 交集
res = set1.intersection(set2)
res = set1 & set2
print(res)

# difference()   差集
res = set1.difference(set2)
res = set2.difference(set1)
res = set1 - set2
print(res)

# union()  并集
res = set1.union(set2)
res = set1 | set2
print(res)

# symmetric_difference() 对称差集 (补集情况涵盖在其中)
res = set1.symmetric_difference(set2)
res = set1 ^ set2
print(res)

setvar = {"刘浩杰", "徐信信", "何伟福", "林志远"}
setvar.add("abcd")
print(setvar)

# update() 迭代着增加
setvar = {"刘浩杰", "徐信信", "何伟福", "林志远"}
lst = ['胡家豪', "胡启超"]
setvar.update(lst)  # 把列表当中的元素一个一个拿出来放进集合中,需要时可迭代性数据
print(setvar)

setvar = {"刘浩杰", "徐信信", "何伟福", "林志远"}
strvar = "abcd"
setvar.update(strvar)
print(setvar)

# remove()  删除集合中指定的值(不存在则报错)
setvar = {"刘浩杰", "徐信信", "何伟福", "林志远"}
setvar.remove("徐信信")
print(setvar)

# discard() 删除集合中指定的值(不存在的不删除 推荐使用)
setvar = {"刘浩杰", "徐信信", "何伟福", "林志远"}
setvar.discard("林志远")
setvar.discard("何伟福121211212")  # 如果这个值不存在,就不删除,也不报错
print(setvar)

# ### 冰冻集合
'''
#frozenset 可强转容器类型数据变为冰冻集合
冰冻集合一旦创建,不能在进行任何修改,只能做交叉并补操作
'''
# 定义一个空冰冻集合
fz = frozenset()
print(fz, type(fz))

fz1 = frozenset([1, "2", 3, 4])
fz2 = frozenset("7892")
print(fz1, fz2)

# 并冻集合只能做交叉并补
res = fz1 & fz2
print(res)
