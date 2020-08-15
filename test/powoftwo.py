#!/usr/bin/env python3

def div(n, q=0):
    if n == 1:
        return q,n
    elif n == 0:
        return q,n
    else:
        q  += 1
        return div(n//2, q)


def nearest(n):
    ''' given input n
        find the nearest power
        of 2 closest to n
    '''
    # q is the number  of time n was divided by 2
    # repeatedly until we get either 1 or 0
    q,r = div(n)
    if r == 1:
        return 2**(q+1)
    else:
        return 2**q


if __name__ == "__main__":
    print(nearest(129))

