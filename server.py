import socket


def Server():
    host = '127.0.0.1'  # Server ip
    port = 65434

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print("Server Started")
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        sock.sendto(data.encode('utf-8'), addr)


if __name__ == '__main__':
    Server()