#!/usr/bin/env python3

import socket
import merkeltree
import os
import sys

def getfile():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            return sys.argv[1]
        else:
            print('No such file, or too many arguments expected only 1 (filename)')
            sys.exit()
    else:
        print('Provide file, please')
        sys.exit()
    
def sender():
    HOST = '127.0.0.1'
    PORT = 65000
    # compute hash on the fly, return root of merkletree
    tree = merkeltree.MerkelTree(getfile())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes.fromhex(tree.treehash()))
        data = s.recv(1024)
        if repr(data) == b'inconsistent':


    print("Received ", repr(data))

if __name__ == '__main__':
    #getfile()
    sender()
