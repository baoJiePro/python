# ### 同一文件的变量缓存机制
'''
变量的缓存机制是为了节省内存空间,提高效率
'''
'''
-->Number 部分
1.对于整型而言，-5~正无穷范围内的相同值 id一致
2.对于浮点数而言，非负数范围内的相同值 id一致
3.布尔值而言,值相同情况下，id一致
4.复数的id标识都不相同(在 实数+虚数 这样的结构中)
'''

intvar1 = 99
intvar2 = 99
intvar1 = -99
intvar2 = -99
print(id(intvar1), id(intvar2))

# 浮点型:非负数
f1 = 3.15
f2 = 3.15
f1 = -3.15
f2 = -3.15
print(id(f1), id(f2))

# 布尔值而言,值相同情况下，id一致
t1 = True
t2 = False
print(id(t1), id(t2))

c1 = 3 - 2j
c2 = 3 - 2j
print(id(c1), id(c2))

# 只有虚数的情况下,在值相同时,地址相同
c1 = 6j
c2 = 6j
print(id(c1), id(c2))

# (1) bool + int
res = True + 89
print(res)

# (2) bool + float
res = True + 55.78
print(res)

# (3) bool + complex
res = False + 2-4j
print(res)

# (4) int  + float
res = 31 + 4.1
print(res)

# (5) int + complex
res = 17 + 4-7j
print(res)

# (6) float + complex
res = 8.12 + 3+5j
print(res)
