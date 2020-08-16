#!/usr/bin/env python3

import hashlib
import sys
sys.path.insert(1, '/Users/aditya/Desktop/languages/python/merkeltree')
import merkeltree

def test_leafnodes():
    ''' test the number of leaf nodes
        number of leaf node hashes = number of MerkelNodes in 
        hashlist 
    '''
    ''' THERE ARE DUPLICATES IN WHEN WE TRAVERSE 
        THE TREE

        DUPLICATES ARE BECAUSE OF THE FACT THAT SOME NODES HASH
        WITH THEMSELVES AS A RESULT THE TRAVERSAL WILL SEE ALL OF 
        THEM INCLUDING THE DUPLICATES
    '''
    tree = merkeltree.MerkelTree()
    print(len(tree.hashlist))
    f = 'hashlist.txt'
    with open(f, 'w') as mf:
        lst = [node.nodehash for node in tree.hashlist]
        for v in lst:
            mf.write(str(v) + '\n')

def test_simpletree():
    ''' test a 3 node merkel tree'''
    ''' UNDERSTOOD WHY THERE ARE SEVERAL DUPLICATES
        (WHEN NOT 2^n). ITS THE REASON THAT YOU GUESSED
        EACH NODE CREATED FROM HASHING ITSELF, SEES ITS 
        CHILDREN IN MULTIPLE OF TWO HENCE FOR EVERY SUCH
        NODE CREATED, WE WILL SEE THE NUMBER OF ITS CHILDREN
        AS 2

        TODO: HOPEFULLY THIS IS NOT GOING TO BE A PROBLEM 
        WHICH VERIFYING THE INTEGRITY OF FILES
        BETWEEN TWO PROCESSES
    '''
    # h1,h2 example hash of file data chunks
    h1 = hashlib.sha256(b'1'*1024).hexdigest()
    h2 = hashlib.sha256(b'2'*1024).hexdigest()
    h3 = hashlib.sha256(b'3'*1024).hexdigest()
    h4 = hashlib.sha256(b'4'*1024).hexdigest()
    h5 = hashlib.sha256(b'5'*1024).hexdigest()

    hs = [h1,h2,h3,h4,h5]
    hl = [merkeltree.MerkelNode(nodehash=i) for i in hs]

    tree = merkeltree.MerkelTree(hl)
    print("TREE HASH: ", tree.treehash())
    tree.traverse()

    #tree.leafNodes()


if __name__ == "__main__":
    #test_leafnodes()
    test_simpletree()
