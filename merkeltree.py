#!/usr/bin/env python3

import hashlib

class Node(object):
    
    def __init__(self, nodehash):
        ''' A node consists of pointer to left subtree
            and right subtree and the combined hash of 
            the root of these two subtrees
        '''
        self.left = None
        self.right = None
        if (self.left == None and self.right == None):
            # if leaf node, then hash is just the
            # nodehash passed to constructor
            self.nodehash == nodehash
        else:
            # else, calculate the hash from the subtrees
            self.nodehash = self.creat_hash()

    def create_hash(self):
        ''' for every node, create the hash '''
        return hashlib.sha256(left.nodehash + right.nodehash)



class MerkelTree(object):

    def __init__(self):
        pass


    pass




if __name__ == "__main__":
    root = Node()
    root.
