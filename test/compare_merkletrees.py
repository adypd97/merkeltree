#!/usr/bin/env python3

import hashlib
import sys
sys.path.insert(1, '/Users/aditya/Desktop/languages/python/merkeltree')
import merkeltree


def compare_return(st, ct):
    ''' compare the hash values for 
        servertree and clienttree,
        construct diff which stores 
        the relevant chunks which differ
        and return it back
    '''
    diff = {}
    st_hashes = st.merkledict.keys()
    ct_hashes = ct.merkledict.keys()
    assert len(st_hashes) == len(ct_hashes)
    for s,c in zip(st_hashes, ct_hashes):
        if s != c:
            if ct.isLeaf(c):
                diff[c] = ct.merkledict[c]
    return diff

if __name__ == '__main__':
    # servertree is ground truth
    servertree = merkeltree.MerkelTree('../serverfile.txt')
    clienttree = merkeltree.MerkelTree('../clientfile.txt')
    diff_chunks = compare_return(servertree, clienttree)
    print(diff_chunks)
