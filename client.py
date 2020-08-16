#!/usr/bin/env python3

import socket

def sender():
    HOST = '127.0.0.1'
    PORT = 65000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello')
        data = s.recv(1024)

    print("Received ", repr(data))

if __name__ == '__main__':
    sender()
