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
    def __init__(self, hash_list):
        self.root = self.gen_tree(hash_list)
        # treeHash is the root hash
        self.treeHash = self.root.nodehash
    
    def gen_tree(self, hl):
        # 1. build tree using hl 
        # where, hl consists of MerkelNodes ^^^
        # 2. every additional level in tree
        #    would also be a MerkelNode
        #    all the way to the root
        tmp = []
        if (len(hl) == 1):
            return hl[0]
        else:
            # if its the leaf nodes
            if len(hl) == XX # XX stands for ini len of hl, 
                             # UPGRADE: right now it needs to be 2^n
                for i in range(0,len(hl),2):
                    tmp.append(


    pass


if __name__ == "__main__":
    # h1,h2 example hash of file data chunks
    h1 = hashlib.sha256(b'1'*1024).digest()
    h2 = hashlib.sha256(b'2'*1024).digest()

    left = MerkelNode(nodehash=h1)
    right = MerkelNode(nodehash=h2)

    root = MerkelNode(left=left, right=right)
    #print(root.nodehash)
    

