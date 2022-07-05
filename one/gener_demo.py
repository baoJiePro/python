def consumer(name):
    print("%s准备吃包子" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了！" % (baozi, name))


c = consumer("andy")

# 只唤醒yield
c.__next__()

b1 = "韭菜馅"
# 给yield传值同时调用yield
c.send(b1)

# c.__next__()

import time


def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子！")
        c.send(i)
        c2.send(i)


# producer("andy")

from collections.abc import Iterable

print(isinstance([], Iterable))

a = [1, 2, 3]

b = iter(a)

print(b.__next__())

print(range(10))

for x in range(10):
    print(x)






