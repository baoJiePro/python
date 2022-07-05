l1 = [1, 2, 3, 4, 5, 4, 7]
l2 = [1, 3, 4, 6, 7, 8, 9]

l1 = set(l1)
l2 = set(l2)
print(l1, type(l1))
print(l2, type(l2))
# 交集
print(l1.intersection(l2))
# 并集
print(l1.union(l2))
# 差集
print(l1.difference(l2))
# 子集
print(l1.issubset(l2))
# 父集
print(l1.issubset(l2))
