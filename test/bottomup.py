#!/usr/bin/env python3

''' Take list of elements in l
    and create a tree out of it
    like so:
            l0
        l1     l1
    1     2  3    4  
'''

# MAYBE REQUIRED
# this looks like a breath search(kind of)
def layer1(l):
    if not l:
        print("*****")
    else:
        print(l)
        layer1(l[:-1])


# BOTTOM UP MERKEL TREE WOULD REQUIRE THIS BLUEPRINT
# TO CONSTRUCT THE TREE
def twoatatimesum1(l):
    s = []
    if (len(l) == 1):
        print(l)
        return 0
    else:
        print(l)
        for i in range(0,len(l),2):
            s.append(l[i] + l[i+1])
        return twoatatimesum1(s)

# NOT REQUIRED
#def twoatatimesum2(l):
#    s = []
#    for i in range(0,len(l),2):
#        s.append(l[i] + l[i+1])
#    return s
#
#def twoatatimesum3(l):
#    s = []
#    if len(l) == 1:
#        return "exiting" 
#    for i in range(0,len(l),2):
#        s.append(l[i] + l[i+1])

if __name__ == "__main__":
    # len(l) must be power of 2
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #layer1(l)
    #twoatatimesum3(twoatatimesum2(twoatatimesum1(l)))
    print("STATUS: ", twoatatimesum1(l))

