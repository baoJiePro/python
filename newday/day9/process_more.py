import multiprocessing
import time


def f(name):
    time.sleep(2)
    print("hello", name)


for i in range(5):
    p = multiprocessing.Process(target=f, args=(i,))
    p.start()
    # p.join()
