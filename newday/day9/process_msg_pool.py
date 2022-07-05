from multiprocessing import Process, Pool
import time
import os


def Foo(i):
    time.sleep(2)
    print(i)
    return i + 100


def Bar(arg):
    print("-->exec done:", os.getpid())


pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)
    # pool.apply(func=Foo, args=(i,)) 串行
print(os.getpid())
print('end')
pool.close()
pool.join()
