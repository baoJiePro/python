import threading
import time

lock = threading.Lock()


def run(n):
    lock.acquire()
    global num
    num += 1
    lock.release()
    print("task ", n)
    time.sleep(2)


# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
#
# t1.start()
# t2.start()
num = 0
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t--%s" % i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("--------all thread have finished", threading.current_thread())
print(num)
