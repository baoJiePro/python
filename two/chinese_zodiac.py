# 记录生肖，根据年份来判断生肖

chinese_odiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

# print(chinese_odiac[0])
# print(chinese_odiac[0:4])
# print(chinese_odiac[-1])

year = 2018

print(year % 12)
print(chinese_odiac[year % 12])

print('狗' in chinese_odiac)
