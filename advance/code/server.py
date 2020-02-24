import socket
''' server.py'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定地址与端口
server.listen()
sock, addr = server.accept()

data = sock.recv(1024)  # 一次接受 1KB 数据
print(data.decode('utf8'))
sock.send(('Hello %s' % data.decode('utf8')).encode('utf8'))
sock.close()
server.close()