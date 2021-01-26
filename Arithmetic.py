from math import *


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0

    a = int(log2(n)) + 1 // 2
    b = int(log2(n)) + 1 % 2

    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
        
        
