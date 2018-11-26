#euler 87

import random
import itertools
from tqdm import tqdm
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


seen = []

for a in tqdm(range(1, 7080)):
	
	if miller(a):
	
		for b in range(1, 370):
		
			if miller(b):
			
				for c in range(1, 90):
					
					if miller(c):
			

						val = a**2 + b**3 + c**4
	
						if val < 50000000:
					
					
							seen.append(val)
					

c = Counter(seen)
	
print(len(c))