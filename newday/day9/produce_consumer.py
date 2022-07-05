import threading
import queue

q = queue.Queue()


def produce():
    for i in range(20):
        q.put("骨头 %s" % i)


def consumer(name):
    while q.qsize() > 0:
        print("[%s]取到[%s]并且吃了它。。。" % (name, q.get()))


p = threading.Thread(target=produce, )
c = threading.Thread(target=consumer, args=("andy",))
p.start()
c.start()
