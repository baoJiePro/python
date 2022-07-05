import threading
import queue
import time

q = queue.Queue(maxsize=10)


def produce():
    count = 1
    while True:
        q.put("骨头 %s" % count)
        print("生产了骨头%s" % count)
        count += 1
        time.sleep(0.3)


def consumer(name):
    while True:
        print("[%s]取到[%s]并且吃了它。。。" % (name, q.get()))
        time.sleep(1)


p = threading.Thread(target=produce, )
c = threading.Thread(target=consumer, args=("andy",))
c1 = threading.Thread(target=consumer, args=("alex",))
p.start()
c.start()
c1.start()
