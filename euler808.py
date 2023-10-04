#euler 808

from math import gcd
import math
import random
import sys
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

def genpsq():

    n = 1

    while True:

        if miller(n):
            yield (n*n)

        n += 1

found = 0
total = 0

for psq in genpsq():

    nums = str(psq)
    numr = nums[::-1]

    #print("Checking if", nums, "and", numr, "are palindromes")

    if nums != numr:

        #print("Checking if the square root of", numr, "(", math.sqrt(int(numr)), ") is prime")
        
        if miller(math.sqrt(int(numr))):

            found += 1
            total += psq


            print(psq, ", found", found, ", total", total)

            if found == 50:
                print("Total =", total)
                input()





        
