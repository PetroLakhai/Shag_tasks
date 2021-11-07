import socket

SECOND_SENDER_NAME = 'Juliet'


def Sender_Juliet(sender_name):
    host = '0.0.0.0'  # client ip
    port = 8002

    server = ('127.0.0.1', 65434)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print('Print "quit" to stop sending messages to server')
    message = input(f'{sender_name} -> ')
    while message != 'quit':
        sock.sendto(message.encode('utf-8'), server)
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print('Received from server last Juliet`s message: ' + data)
        message = input(f'{sender_name} -> ')
    sock.close()


if __name__ == '__main__':
    Sender_Juliet(SECOND_SENDER_NAME)
