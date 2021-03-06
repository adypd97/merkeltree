#!/usr/bin/env python3

import hashlib
import os
from treeError import TreeEmptyError

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
        Root hash represents entire file's hash
    '''
    def __init__(self, filename):
        #self.root = self.gen_tree(datalst)
        self.datalist = self.gen_datalist(filename)
        self.hashlist = self.gen_hashlist(self.datalist)
        self.dictionary = self.gen_hash_to_datachunk_dict()
        self.root = self.gen_tree(self.hashlist)
        self.treeHash = self.root.nodehash

        # REFACTOR THIS
        self.nodehashdict = {}
        self.gen_nodehashdict(self.nodehashdict)

        # merkledict represents the complete merkletree
        self.merkledict = self.gen_merkledict()

    
    def get_children_of_node(self, hashval):
        if hashval in self.nodehashdict.keys():
            return self.nodehashdict[hashval]
        else:
            raise KeyError('No such key')

    def gen_merkledict(self):
        return dict(self.nodehashdict, **self.dictionary)
    
    def get_nodehashdict(self):
        return self.nodehashdict

    def get_hash(self, index):
        assert index < len(self.hashlist)
        return self.hashlist[index].nodehash

    def get_datachunk(self, index):
        assert index < len(self.datalist)
        return self.datalist[index]

    def treehash(self):
        return self.treeHash

    def gen_hash_to_datachunk_dict(self):
        ''' generate a dictionary with 
            key = chunk hash and value = chunk of data
        '''
        dictionary = {}
        assert len(self.datalist) == len(self.hashlist)
        for i in range(len(self.datalist)):
            dictionary[self.get_hash(i)] = self.get_datachunk(i)
        return dictionary

    def get_datachunk_for_hash(self, hashval):
        ''' return dictionary generated by
            self.gen_hash_to_datachunk_dict()
        '''
        if hashval in self.dictionary.keys():
            return self.dictionary[hashval]
        else:
            raise KeyError('No such key')

    def gen_datalist(self, f='clientfile.txt'):
        if os.path.exists(f):
            CHUNK_SIZE=1024  # bytes , 1KB
            datalist=[]
            with open(f, 'rb') as merfile:
                while True:
                    data = merfile.read(CHUNK_SIZE)
                    if data == b'' :
                        break
                    datalist.append(data) # read 1024 bytes in one chunk
        else:
            raise FileNotFoundError('File doesnt exist')
        
        return datalist
    
    def gen_hashlist(self, datalist):
        ''' input: datlist
            consists of data from 
            file partitioned into chunks
            for hashing
        '''
        hashlist = []
        for chunk in datalist:
            sha = hashlib.sha256()
            sha.update(str(chunk).encode('utf-8'))
            nodehash = sha.hexdigest()
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
        if len(hl) == 0:
            raise TreeEmptyError('Hashlist is empty')
        if len(hl) == 1:
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
            return self.gen_tree(tmp)

    def gen_nodehashdict(self, d):
        if self.root is not None:
            self._gen_nodehashdict(self.root, self.nodehashdict)
        else:
            raise TreeEmptyError('Tree doesnt exist')
        
    def _gen_nodehashdict(self, node, d):
        if node.left is not None and node.right is not None:
            #print(len(d.keys()))
            self._gen_nodehashdict(node.left, d)
            d[node.nodehash] = [node.left.nodehash, node.right.nodehash]
            self._gen_nodehashdict(node.right, d)

    '''
    def leafNodes(self):
        # return a list of leaf nodes
        if self.root is not None:
            self._leafNodes(self.root)
        else:
            raise TreeEmptyError("Tree doesn't exist")

    def _leafNodes(self, node):
        if node.left == None and node.right == None:
            self.printNode(node)
            return
        else:
            self._leafNodes(node.left)
            self._leafNodes(node.right)
    '''


    def traverse(self):
        ''' compare hash of two different merkel trees
            for data integrity checks,
        '''
        if self.root is not None:
            self._traverse(self.root)
        else:
            raise TreeEmptyError("Tree doesn't exist")

    def _traverse(self, node):
        if node is not None:
            self._traverse(node.left)
            self.printNode(node)
            self._traverse(node.right)

    def printNode(self, node):
        print("NODE HASH: ", node.nodehash)

    def isLeaf(self, hashval):
        ''' given hashval, is it leaf node '''
        return hashval in self.dictionary.keys()



if __name__ == "__main__":
    tree = MerkelTree('clientfile.txt')

    # TODO: Check correctness of traverse()
    # looks like its should be less because we only create 
    # 87 + 44 + 22 + 11 + 6 + 3 + 2 + 1 = 176 nodes

    # its greater than 176 because some nodes hash with themselves
    #tree.traverse()
    #tree.leafNodes()
    #print(tree.treehash())
    #hashval = tree.get_hash(0)
    #print(hashval)
    #print(tree.dictionary.keys())
    #print(tree.get_datachunk_for_hash(hashval) == tree.get_datachunk(0))
    #children = tree.get_children_of_node(tree.treehash())
    #expected_children = [tree.root.left.nodehash, tree.root.right.nodehash]
    #print(len(tree.merkledict.keys()))


    '''
    # h1,h2 example hash of file data chunks
    h1 = hashlib.sha256(b'1'*1024).digest()
    h2 = hashlib.sha256(b'2'*1024).digest()
    h3 = hashlib.sha256(b'3'*1024).digest()

    left = MerkelNode(nodehash=h1)
    middle = MerkelNode(nodehash=h2)
    right = MerkelNode(nodehash=h3)
    hl = [left, middle, right]

    tree = MerkelTree(hl)
    #print("TREE HASH: ", tree.treehash())
    tree.traverse()

    hl_1 = [left, middle]
    tree_1 = MerkelTree(hl_1)
    #print("LEFT ", tree_1.root.nodehash == tree.root.left.nodehash)

    hl_2 = [right, right]
    tree_2 = MerkelTree(hl_2)
    #print(tree_2.root.nodehash)
    #print(tree.root.right.nodehash)
    #print("RIGHT ", tree_2.root.nodehash == tree.root.right.nodehash)

    hl_3 = [tree_1.root, tree_2.root]
    final = MerkelTree(hl_3)
    #print("FINAL ", final.root.nodehash == tree.root.nodehash)
    '''
