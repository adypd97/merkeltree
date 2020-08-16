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

                if check_hash(data.hex()):
                    conn.sendall(b'consistent')
                else:
                    conn.sendall(b'inconsistent')

def check_hash(FileHash):
    EXPECTED_HASH='f5804d45cef78123799c59f70efdad565bbaf339ecb041fa7e051e6fcee77f3b'
    return FileHash == EXPECTED_HASH

if __name__ == '__main__':
    listener()


