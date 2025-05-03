#euler 204

import math
import sys
from tqdm import tqdm
import ast
import random
from bitarray import bitarray

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
    
#primes = []
limit = 10**9
#test = limit

#f = open("primes.txt", 'w')

#while test >= 2:

#    if miller(test):
    
        #primes.append(test)
#        f.write(f"{test}\n")
    
#    test -= 1

#print("Loading primes...")

#f = open("primes.txt", "r")
#primes = [int(line.strip()) for line in f]
#print("...done")

f = open("primes.txt", "r")

H = 100

exclude = 0
seen = bitarray(limit + 1)
seen.setall(False)

for line in f:

    p = int(line.strip())
    num = p
    
    if num > H:
        
        sys.stdout.write("\r" + "Prime factor: " + str(num) + "                    ")
        sys.stdout.flush()
        
        while num <= limit:
    
            if not seen[num]:
                exclude += 1
                seen[num] = True
            
            num += p


print()
print(limit-exclude)        
