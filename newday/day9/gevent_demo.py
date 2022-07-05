import gevent
import datetime


def func1():
    print(str(datetime.datetime.now()) + '\033[31;1m哈哈111111.。。。。、\033[0m')
    gevent.sleep(2)
    print(str(datetime.datetime.now()) + '\033[31;1m哈哈3333333.。。。。、\033[0m')


def func2():
    print(str(datetime.datetime.now()) + '\033[32;1m哈哈222222.。。。。、\033[0m')
    gevent.sleep(3)
    print(str(datetime.datetime.now()) + '\033[32;1m哈哈4444444.。。。。、\033[0m')


def func3():
    print(str(datetime.datetime.now()) + '\033[33;1m哈哈5555555.。。。。、\033[0m')
    gevent.sleep(1)
    print(str(datetime.datetime.now()) + '\033[33;1m哈哈6666666.。。。。、\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])
