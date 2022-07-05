import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num


    def run(self) -> None:
        print("running on number:%s" %self.num)
        time.sleep(3)



t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t2.start()
