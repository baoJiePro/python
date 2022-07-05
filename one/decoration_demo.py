# 装饰器：本质是函数，就是为其他函数添加附加功能
# 原则：1.不能修改被装饰的函数的源代码，2. 不能修改被装饰的函数的调用方式
# 知识储备：
# 1. 函数即"变量" 2. 高阶函数 3. 嵌套函数

import time


def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time - start_time))

    return warpper


@timmer
def test1():
    time.sleep(3)
    print("test1")


# test1()

user, passwd = "bj", "123456"


def auth(auth_type):
    print("auth_type:", auth_type)

    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    func(*args, **kwargs)
                else:
                    exit()
            elif auth_type == "ldap":
                username = input("username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    func(*args, **kwargs)
                    print("ldap登录测试")
                else:
                    exit()

        return wrapper

    return outer_wrapper


def index():
    print("index")


@auth(auth_type="local")
def home():
    print("home")


@auth(auth_type="ldap")
def bbs():
    print("bbs")

index()

home()

bbs()
