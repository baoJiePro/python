# 列表生成式
list = [i * 2 for i in range(10)]
print(list)

# 在调用时才会生成相应的数据,只记录当前位置，只有一个__next__()方法
b = (i * 2 for i in range(10))

# for i in b:
#     print(i)

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())