#!/usr/bin/env python3

import socket
import merkeltree
import os
import sys

# tryhashes
# if the root hash fails
# then,
# send the remaining merkledict keys to the server
# the server checks each key to find out which chunks needs to be 
# returned
# client waits for the chunks to be returned, on receiving them
# it replaces the chunks in the file.
# finally, it sends the recomputed merkleroot hash for the updated
# file to server for checking to recheck consistency,
# then it terminates
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
        # first try merkleroot
        s.sendall(bytes.fromhex(tree.treehash()))
        data = s.recv(1024)
        if data.decode('utf-8') == 'inconsistent':
            print("BAAB")
            # send the merkledict
            # ===> s.sendall(tree.merkledict)
            # now receive the chunks 
            # then, recompute updated hash
            # finally, send this hash back
            # to recheck consistency
            # exit.

    print("Received ", repr(data))

if __name__ == '__main__':
    #getfile()
    sender()
