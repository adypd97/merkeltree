#!/usr/bin/env python3

import hashlib

''' TODO: We need to build a merkel tree from the bottom up till we 
    reach the root
'''

class MerkelNode(object):
    
    def __init__(self, left=None, right=None, nodehash=b''):
        ''' A node consists of pointer to left subtree
            and right subtree and the combined hash of 
            the root of these two subtrees
        '''
        self.left = left
        self.right = left
        if (nodehash):
            # if leaf node, then hash is just the
            # nodehash passed to constructor
            self.nodehash = nodehash
        else:
            # else, calculate the hash from the subtrees
            self.nodehash = self.create_hash()

    def create_hash(self):
        ''' for every node, create the hash '''
        return hashlib.sha256(left.nodehash + right.nodehash).hexdigest()



class MerkelTree(object):
    ''' Binary Merkel Tree consisting of Merkel Node ^^^^
        TODO: HOW TO STORE THE FINAL MERKEL TREE?
    '''
    def __init__(self, datalst):
        self.root = self.gen_tree(self.gen_hashlist(self.gen_datalist()))
        # treeHash is the root hash
        self.treeHash = self.root.nodehash

    def gen_datalist(f='merkelfile.txt'):
        CHUNK_SIZE=1024  # bytes , 1KB
        CHUNKS=[]
        with open(f, 'rb') as merfile:
            while True:
                data = merfile.read(CHUNK_SIZE)
                if data == b'' :
                    break
                CHUNKS.append(data) # read 1024 bytes in one chunk
        # TODO: make len(CHUNKS) = 2^n
        return CHUNKS
    
    def gen_hashlist(self, datalst):
        ''' datalst is a list of len = 2^n
            which consists of data from 
            file partitioned into chunks
            for hashing
        '''
        # leaft nodes of MerkelTree generation
        hashlist = []
        # assert here that len(datalst) = 2^n
        for chunk in datalst:
            nodehash = hashlib.sha256(chunk).digest()
            hashlist.append(MerkelNode(nodehash=nodehash))
        return hashlist

    def gen_tree(self, hl):
        ''' 1. build tree using hl 
         where, hl consists of MerkelNodes ^^^
         generated from data chunks of a file
         2. every additional level in tree
            would also be a MerkelNode
            all the way to the root
        '''
        # TODO: Has this created a MerkelTree?
        # ie. can i reach any node from self.root after
        # this procedure is over.
        tmp = []
        if (len(hl) == 1):
            # this is root of merkel tree
            return hl[0]
        else:
            print(hl)
            # if its the leaf nodes
            # TODO: if len(hl) == XX # XX stands for ini len of hl, 
                             # UPGRADE: right now it needs to be 2^n
            for i in range(0,len(hl),2):
                tmp.append(MerkelNode(left=hl[i], right=hl[i+1]))
            return self.gen_tree(tmp)

    def traverse_from_root(self):
        ''' compare hash of two different merkel trees
            for data integrity checks,
        '''
        pass

if __name__ == "__main__":
    # h1,h2 example hash of file data chunks
    h1 = hashlib.sha256(b'1'*1024).digest()
    h2 = hashlib.sha256(b'2'*1024).digest()

    left = MerkelNode(nodehash=h1)
    right = MerkelNode(nodehash=h2)

    root = MerkelNode(left=left, right=right)
    #print(root.nodehash)
    

