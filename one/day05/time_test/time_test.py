import time

# 秒为单位
print(time.time())

print(time.localtime())

# help(time)

print(time.timezone)

x = time.localtime()

# 将元组转换为格式化日期
y = time.strftime('%Y-%m-%d %H:%M:%S', x)
print(y)

print(time.asctime())

print(time.ctime())

import datetime

# 3天后
print(datetime.datetime.now() + datetime.timedelta(3))
# 3天前
print(datetime.datetime.now() - datetime.timedelta(3))

import random

print(random.random())
# 123
print(random.randint(1, 3))
# 12
print(random.randrange(1, 3))

print(random.choice('hello'))

print(random.sample('hello', 2))

print(random.uniform(1, 3))

# print(random.shuffle([1, 2, 3, 4, 5]))


# 获取随机验证码
checkCode = ''

for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    checkCode += str(tmp)
print(checkCode)
