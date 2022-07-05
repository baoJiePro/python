import threading
import time


def run(n):
    print("task ", n)
    time.sleep(2)


# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
#
# t1.start()
# t2.start()

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t--%s" % i,))
    # 把当前线程设置为守护线程，无关紧要
    t.setDaemon(True)
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("--------all thread have finished", threading.current_thread())
print("cost:", time.time() - start_time)
