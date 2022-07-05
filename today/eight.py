i = 0
# while i <= 100:
#     print(i)
#     i += 1

# help(print)
while i < 10:
    print("*", end="")
    i += 1
print("----------")
# 字符串的切片简而言之就是字符串的截取操作
strvar = "五一假期,国家法定多放假了一天,大家莆田同庆,一起欢度美好时光"
# (1)[开始索引:]  从开始索引截取到字符串的最后
res = strvar[23:]
print(res)
# (2)[:结束索引]  从开头截取到结束索引之前(结束索引-1)
# 注意:高位取不到
res = strvar[:4]
print(res)
res = strvar[5:9]
print(res)

res = strvar[0:]
print(res)

# for i in strvar:
#     print(i)

dictvar = {'a': 1, 'b': 2, 'c': 3}
for key in dictvar:
    print(key)

strvar = "{}向{}开了一枪,饮弹而亡"
res = strvar.format("11", "22")
print(res)

strvar = "{1}给{0}一个大大的拥抱,幸福温暖"
res = strvar.format("11", "22")
print(res)

strvar = "{who1}向{who2}进行扫射,浑身都是弹孔"
res = strvar.format(who1="11", who2="22")
print(res)
