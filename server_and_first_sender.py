import socket
from threading import Thread

FIRST_SENDER_NAME = 'Romeo'


def Server():
    host = '127.0.0.1'  # Server ip
    port = 65434

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print("Server Started")
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print(f"Message from sender {addr}: {data}")
        print(f"Sending message to sender: {data} \n")
        sock.sendto(data.encode('utf-8'), addr)


def Sender_Romeo(sender_name):
    host = '0.0.0.0'  # client ip
    port = 8001

    server = ('127.0.0.1', 65434)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print('Print "quit" to stop sending messages to server')
    message = input(f'{sender_name} -> ')
    while message != 'quit':
        sock.sendto(message.encode('utf-8'), server)
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print('Received from server last Romeo`s message: ' + data)
        message = input(f'{sender_name} -> ')
    sock.close()


if __name__ == '__main__':
    Thread(target=Server).start()
    Thread(target=Sender_Romeo, args=(FIRST_SENDER_NAME, )).start()

