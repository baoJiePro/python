class Foo:

    def __init__(self):
        pass

    # 对象加()执行该方法
    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__

# 打印类中所有属性
print(Foo.__dict__)
print(obj.__dict__)


# class Foo(object):
#
#     def __getitem__(self, key):
#         print('__getitem__', key)
#
#     def __setitem__(self, key, value):
#         print('__setitem__', key, value)
#
#     def __delitem__(self, key):
#         print('__delitem__', key)
#
#
# obj = Foo()
#
# result = obj['k1']  # 自动触发执行 __getitem__
# obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# del obj['k1']

def func(self):
    print('hello wupeiqi')


def __init__(self, name, age):
    self.name = name
    self.age = age


Foo = type('Foo', (object,), {'func': func, '__init__': __init__})

# Foo = type('Foo', (object,), {'func': func})
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员

f = Foo("alex", 25)