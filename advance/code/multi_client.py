import socket
''' multi_client.py'''
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
client.send('Connect'.encode('utf8'))
while True: 
    message = input()
    client.send(message.encode('utf8'))
    data = client.recv(1024)
    accept_str = data.decode('utf8')
    if accept_str == 'disconnect':
        break
    print(accept_str)
print('disconnect')
client.close()