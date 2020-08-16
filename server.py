#!/usr/bin/env python3

import socket
import merkeltree

def listener():
    HOST = '127.0.0.1'
    PORT = 65000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connection from ", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == '__main__':
    listener()


