import socket

# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 9999)
print('正在连接 %s 端口...' % server_address[1])
client_socket.connect(server_address)

while True:
    try:
        # 发送数据给服务器
        message = input('你好，服务器！\n')
        if message == 'quit':
            exit()
        print('发送数据:', message)
        client_socket.sendall(message.encode())

        # 接收服务器的响应
        data = client_socket.recv(1024)
        print('收到服务器的响应:', data.decode())

    finally:
        # 关闭连接
        pass
        # print('关闭连接')
        # client_socket.close()