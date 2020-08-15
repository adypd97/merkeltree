#!/usr/bin/env python3

import hashlib


def nodehash(h1, h2):
    ''' provide two hashes 
        input:  h1 and h2
        
        compute the hash of the 
        sum of the two hashes

        return: h

    '''
    sha = hashlib.sha256()
    sha.update(h1 + h2)

    return sha.hexdigest()





if __name__ == "__main__":
    h1 = hashlib.sha256(b'1'*1024).digest()
    h2 = hashlib.sha256(b'2'*1024).digest()
    print(nodehash(h1,h2))
    



