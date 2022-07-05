def test():
    '''testing'''
    print("in the test")
    return 0


def test2():
    '''testing'''
    print("in the test2")


x = test()
y = test2()

print(x, y)

import time


def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("a.txt", mode="a", encoding="utf-8") as f:
        f.write("%s end action\n" % time_current)


def test3():
    print("in the test3")
    logger()


def test4():
    print("in the test4")
    logger()


def test5():
    print("in the test5")
    logger()


# test3()
# test4()
# test5()


def test6(x, y, z):
    print(x)
    print(y)
    print(z)


# test6(1, y=2, z=3)

def test7(x, y=2):
    print(x)
    print(y)


# test7(1)


def test8(*args):
    print(args)


test8(1, 2)


def test9(x, *args):
    print(x)
    print(args)


test9(1, 2, 3, 4)


def test10(**kwargs):
    print(kwargs)


test10(name='alex', age=8, sex='M')


def test11(name, **kwargs):
    print(name)
    print(kwargs)


test11("aa", age=18)
