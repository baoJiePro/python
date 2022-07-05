import threading
import time
import random

event = threading.Event()


def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on ---\033[0m')
        elif count < 13:
            print('\033[43;1m--yellow light on ---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on ---\033[0m')
        else:
            count = 0
            event.set()

        time.sleep(1)
        count += 1
 

def car(n):
    while True:
        time.sleep(random.randrange(10))
        if event.isSet():
            print("car [%s] is running..." % n)
        else:
            print("car [%s] is waiting for the red light..." % n)


lightD = threading.Thread(target=light)
lightD.start()

for i in range(3):
    t = threading.Thread(target=car, args=(i,))
    t.start()
