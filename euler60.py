#euler 60
#Takes about 7 hours...

from tqdm import tqdm
import math
import itertools
import random

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

def all_concats_prime(primes):
	for perm in itertools.permutations(primes, 2):
		str_perm = str(perm[0]) + str(perm[1])
		num = int(str_perm)
		if not miller(num):
			return False
				
	return True

			
plist = []
t = 1

while t < 10000:
	if miller(t):
		plist.append(t)
	t += 1

print("Finding pairs")
two_primes = []

for p in tqdm(plist):
	for q in plist:
		if p !=q:
			if all_concats_prime([p, q]):
				two_primes.append([p, q])

print("Finding triples")				
				
three_primes = []
				
for pair in tqdm(two_primes):
	for p in plist:
		test3 = pair + [p]
		if all_concats_prime(test3):
			three_primes.append(test3)

print("Finding quadruples")
				
four_primes = []

for triple in tqdm(three_primes):
	for p in plist:
		test4 = triple + [p]
		if all_concats_prime(test4):
			four_primes.append(test4)
				
print(four_primes)

five_primes = []

for four in tqdm(four_primes):
	for p in plist:
		test5 = four + [p]
		if all_concats_prime(test5):
			five_primes.append(test5)
			
print(five_primes)
			