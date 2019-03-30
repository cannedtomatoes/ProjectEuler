#euler 51 test

import random
import itertools
from tqdm import tqdm

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


print("Generating primes...")
		
primes = []	
for i in range(100000, 1000000):
	if(miller(i)):
		primes.append(i)

p_lists = []
positions = [0, 1, 2, 3, 4, 5]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Generating families...")

for p in primes:
	
	p_list = list(str(p))
	
	for j in range(2, 6):
		
		for c in itertools.combinations(positions, j): 
		
			new = p_list.copy()
			
			for pos in c:
				new[pos] = '*'
			
			family = []
			
			for d in digits:
				
				newnew = new.copy()
				
				for i, n in enumerate(newnew):
					
					if n == '*':
						newnew[i] = d
						
				final_num = int(''.join(newnew))
				
				if miller(final_num) and final_num > 100000:
					family.append(final_num)

			if(len(family)) == 8:
				print(family)
		