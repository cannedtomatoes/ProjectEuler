#euler 131

import math
import sys
from tqdm import tqdm
import ast
import random
import sympy
from collections import Counter


def miller(n):

    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True

def solve(limit):
    

    n = 1
    total = 0
    result = 0

    while True:

        test = (n+1)**3 - n**3

        if test > limit:
            return total
        else:

            if miller(test):        

                total += 1

                print(test, total)

        n += 1

solve(1000000)

    

