import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()


# 信号量，连接池 同一时刻只会有3个线程
semaphore = threading.BoundedSemaphore(3)
for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()

while threading.active_count() != 1:
    pass
else:
    print('------all threads done -----')
