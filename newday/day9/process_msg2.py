from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    print(conn.recv())
    # print(conn.recv())


parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
print(parent_conn.recv())
parent_conn.send("你好，孩子")
# parent_conn.send("哈哈")
p.join()

