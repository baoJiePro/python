# 文件句柄
f = open("fileDemo", mode="r", encoding='utf-8')
# data = f.read()
# print(data)

# for i in range(3):
#     print(f.readline())

# print(f.readlines())

# f.tell()
# 光标移动的位置
# f.seek(0)

# 单行读
# count = 0
# for line in f:
#     if count == 9:
#         print("------分割线------")
#         count += 1
#         continue
#     print(line.strip())
#     count += 1
#
# print(f.encoding)
# print(f.name)

# 截断文字位置
# f.truncate(10)

# 内存开销大
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print("------分割线------")
#         continue
#     print(line.strip())


# f2 = open("fileDemo2", mode="a", encoding="utf-8")
# f2.write('我爱北京天安门\n')
# f2.write("天安门上太阳升\n")

# 读写
# f3 = open("fileDemo2", mode="r+", encoding="utf-8")

# 写读 重新创建文件写
# f3 = open("fileDemo2", mode="w+", encoding="utf-8")

# print(f3.readline())
# print(f3.readline())
# print(f3.readline())
# f3.write("-----hao----")
# print(f3.readline())

f4 = open("fileDemo2", mode="r", encoding="utf-8")
f5 = open("fileDemo3", mode="w", encoding="utf-8")

for line in f4:
    if "中国人民的决心" in line:
        line = line.replace("中国人民的决心", "中国人民的决心!加油")
    f5.write(line)
f4.close()
f5.close()

# 可以自动关闭
with open("fileDemo3", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


import sys
print(sys.getdefaultencoding())