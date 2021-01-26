from math import *
def cont_frac(x : int, y : int) -> int:
    """
    Convert a rational x/y fraction into
    a list of partial quotients [a0, ... , an]
    """

    L = []
    a = x
    b = y
    r = log2(y) #Maximum partial quotients

    while(a%b != 0 and r > 0 ):
        q = a // b
        a_t = a
        a = b
        b = a_t % b
        L.append(q)
        r = r-1

    L.append(a // b)
    

    return L



def compute_frac(l : list) -> tuple:
    """
    compute symbolically a sequence of fractions
    """

    i = len(l)-2
    print (l)
    c = 1
    a = l[i]
    b = l[i+1]

    while ( i > 0 ) :
        a = l[i]
        a = a * b + c
        c = b
        b = a
        i = i - 1
    
    a = l[0]
    a = a * b + c
    

    return (a,b)


def frac_seq(L : list) -> list:
    """
    Give the fractional sequence from a list of partial quotient
    """
    
    seq = []

    for i in range(len(L)) :
        l = L[0:i]
        if len(l) == 0 :
            continue
        elif len(l) == 1 :
            seq.insert(i,(L[0],1))
        else :
            seq.insert(i,compute_frac(l))
    return seq