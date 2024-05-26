import socket

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_address = ('localhost',9999)
print('开始监听 %s 端口...' % server_address[1])
server_socket.bind(server_address)

# 开始监听连接
server_socket.listen(1)

while True:
    # 等待客户端连接
    print('等待连接...')
    connection, client_address = server_socket.accept()
    print('[退出输入quit]\n是否退出:\n')
    qu = input()
    if qu == 'quit':
        exit()
    try:
        print('连接来自', client_address)

        # 接收客户端发送的数据
        while True:
            data = connection.recv(1024)
            print('收到数据:', data.decode())
            if not data:
                break

            # 发送响应给客户端
            message = input('please input your message: ')
            print('发送数据:', message)
            connection.sendall(message.encode())
            # connection.sendall(message.encode('utf-8f'))
            # connection.sendall(b'hello world')
    finally:
        # 关闭连接
        connection.close()