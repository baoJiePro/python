import socket
# 声明socket类型，同时生成socket连接对象
client = socket.socket()

client.connect(('localhost', 6969))

# client.send(b"hello world!")

# client.send('我要传中文'.encode('utf-8'))

while True:
    # msg = input(">>: ").strip()
    # client.send(msg.encode('utf-8'))
    # print('client-->')
    # data = client.recv(1024)
    # print(data.decode())
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode())

    cmd_res = client.recv(1024)
    print(cmd_res)

client.close()




