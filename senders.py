import socket
from threading import Thread

FIRST_SENDER_NAME = 'Mykola'
SECOND_SENDER_NAME = 'Petro'


def Sender(sender_name):
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
        print('Received from server: ' + data)
        message = input(f'{sender_name} -> ')
    sock.close()


if __name__ == '__main__':
    cycle = True
    while cycle:
        print(f'Messages to server from {FIRST_SENDER_NAME}')
        Thread(target=Sender(FIRST_SENDER_NAME)).start()
        print(f'Messages to server from {SECOND_SENDER_NAME}')
        Thread(target=Sender(SECOND_SENDER_NAME)).start()

