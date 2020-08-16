#!/usr/bin/env python3

import socket
import merkeltree
from client import getfile
'''
class Socket():
    HOST = '127.0.0.1'
    PORT = 65000
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        return self.socket.connect((self.HOST, self.PORT))

    def send_data(self, data):
        self.socket.sendall(bytes.fromhex(data))


    def receive_data(self):
        data = self.socket.recv(1024)
        self.check(data.decode('utf-8'))

    def check(self, data):
        if data == 'inconsistent':
            print("BAAD")
        else:
            print("Received ", data)
'''

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
    # compute the hash and assign EXPECTED_HASH with that value
    # obviously we are simulating here, so we will end up reading
    # the same file as client
    # But, it is supposed to work when the two files might be different
    # computers and they are communicating with each other to match
    # the consistency such that both have the same version of the file.
    tree = merkeltree.MerkelTree(getfile())
    EXPECTED_HASH = tree.treehash()
    return FileHash == EXPECTED_HASH

if __name__ == '__main__':
    listener()


