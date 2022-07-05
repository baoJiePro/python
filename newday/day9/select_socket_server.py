import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 不阻塞
server.setblocking(False)
server.bind(('localhost', 10000))
server.listen(100)

inputs = [server]
outputs = []

msg_dic = {}

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:
            conn, addr = server.accept()
            print("来了新链接", addr)
            inputs.append(conn)
            msg_dic[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            print("收到数据", data)
            # r.send(data)
            # print("send done...")
            # print("recv: ", conn.recv(1024))
            msg_dic[r].put(data)
            outputs.append(r)

    for w in writeable:
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)
        outputs.remove(w)


    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)
        del msg_dic[e]
