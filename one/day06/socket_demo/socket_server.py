import socket, os

server = socket.socket()

server.bind(('localhost', 6969))

server.listen(5)

while True:
    # 被动接受TCP客户的连接,(阻塞式)等待连接的到来
    conn, addr = server.accept()
    print("new conn:", addr)

    while True:
        data = conn.recv(1024)
        print('server-->', data.decode())
        if not data:
            print("客户端已断开")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data).read()
        conn.send(cmd_res)
    conn.close()
    server.close()



