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
