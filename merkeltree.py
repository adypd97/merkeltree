#!/usr/bin/env python3

import hashlib
from pprint import pprint

''' TODO: We need to build a merkel tree from the bottom up till we 
    reach the root
'''
class TreeEmptyError(Exception):
    def __init__(self, *args):
        if args:
            self.error = args[0]
        else:
            self.error = None
    def __str__(self):
        if self.error:
            return 'TreeEmptyError, {0}'.format(self.error)
        else:
            return 'TreeEmptyError was raised'


class MerkelNode(object):
    
    def __init__(self, left=None, right=None, nodehash=b''):
        ''' A node consists of pointer to left subtree
            and right subtree and the combined hash of 
            the root of these two subtrees
        '''
        self.left = left
        self.right = right
        if (nodehash):
            # if leaf node, then hash is just the
            # nodehash passed to constructor
            self.nodehash = nodehash
        else:
            # else, calculate the hash from the subtrees
            self.nodehash = self.create_hash()

    def create_hash(self):
        ''' for every node, create the hash '''
        sha = hashlib.sha256()
        sha.update(str(self.left.nodehash).encode('utf-8'))
        sha.update(str(self.right.nodehash).encode('utf-8'))
        return sha.hexdigest()



class MerkelTree(object):
    ''' Binary Merkel Tree consisting of Merkel Node ^^^^
        TODO: HOW TO STORE THE FINAL MERKEL TREE?
    '''
    def __init__(self, datalst):
        #self.root = self.gen_tree(self.gen_hashlist(self.gen_datalist()))
        self.root = self.gen_tree(datalst)
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
        tmp = []
        if (len(hl) == 0):
            raise TreeEmptyError('Hashlist is empty')
        if (len(hl) == 1):
            # this is root of merkel tree
            return hl[0]
        else:
            if len(hl) % 2 == 0:
                for i in range(0,len(hl)-1):
                    if i % 2 != 0:
                        continue
                    tmp.append(MerkelNode(left=hl[i], right=hl[i+1]))
            # if len is odd, take double hash for last element in hl with itself.
            else:
                for i in range(0,len(hl)-2):
                    if i % 2 != 0:
                        continue
                    tmp.append(MerkelNode(left=hl[i], right=hl[i+1]))
                tmp.append(MerkelNode(left=hl[len(hl)-1], right=hl[len(hl)-1]))
            #pprint([o for o in hl])
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
    h3 = hashlib.sha256(b'3'*1024).digest()

    left = MerkelNode(nodehash=h1)
    middle = MerkelNode(nodehash=h2)
    right = MerkelNode(nodehash=h3)
    
    hl = [left, middle, right]

    tree = MerkelTree(hl)

    print(tree.treeHash)
'''
    hl_1 = [left, middle]
    tree_1 = MerkelTree(hl_1)
    print("LEFT ", tree_1.root.nodehash == tree.root.left.nodehash)

    hl_2 = [right, right]
    tree_2 = MerkelTree(hl_2)
    print(tree_2.root.nodehash)
    print(tree.root.right.nodehash)
    print("RIGHT ", tree_2.root.nodehash == tree.root.right.nodehash)

    hl_3 = [tree_1.root, tree_2.root]
    final = MerkelTree(hl_3)
    print("FINAL ", final.root.nodehash == tree.root.nodehash)
'''
