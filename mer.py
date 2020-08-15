#!/usr/bin/env python3

import hashlib

def chunk(f='merkelfile.txt'):
    CHUNK_SIZE=1024  # bytes , 1KB
    CHUNKS=[]
    with open(f, 'rb') as merfile:
        while True:
            data = merfile.read(CHUNK_SIZE)
            if data == b'' :
                break
            CHUNKS.append(data) # read 1024 bytes in one chunk
    return CHUNKS


def hash_chunks(l):
    ''' takes a list of file chunks 'l'
        and produces a hash for all of them
        returning the hash list
    '''
    hash_l = []
    for c in l:
        hash_l.append(hashlib.sha256(c).hexdigest())
    return hash_l

def merkeltree(hl):
    ''' takes a hash list of chunked data
        and produces the ground truth merkel 
        tree
    '''
    pass


if __name__ == "__main__":
    hl = hash_chunks(chunk())
    print(len(hl))


