import socket
import threading
''' server_multi_client.py'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定地址与端口
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)  # 一次接受 1KB 数据
        accept_str = data.decode('utf8')
        if accept_str == 'exit':
            break
        else:
            print(accept_str)
        message = input()
        sock.send(message.encode('utf8'))
    sock.send('disconnect'.encode('utf8'))
    sock.close()


while True:
    sock, addr = server.accept()
    client_threading = threading.Thread(target=handle_sock, args=(sock, addr))
    client_threading.start()