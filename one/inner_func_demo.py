# 0为假
print(all([1, -5, 3]))
# 为空返回假
print(any([]))
# 转二进制
print(bin(10))

# lambda n:print(n)

calc = lambda n: print(n)

calc(5)

import sys

res = filter(lambda n: n > 5, range(10))
for i in res:
    print(i)

data = map(lambda n: n * 5, range(10))
for j in data:
    sys.stdout.write(str(j))
    sys.stdout.write(",")

import functools

res = functools.reduce(lambda x, y: x + y, range(10))

print(res)

a = {6: 2, 1: 3, 2: 8, -5: 10, 99: 14, 33: 22}
print(a)

print(sorted(a))
# key排序
print(sorted(a.items()))
# value排序
print(sorted(a.items(), key=lambda x: x[1]))
