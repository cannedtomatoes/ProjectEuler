#euler 124

from tqdm import tqdm
from math import gcd
import random
from queue import Queue
import sys
from operator import itemgetter

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

def pollard_rho(N):
	if N % 2 == 0:
		return 2
	x = random.randint(1, N-1)
	y = x
	c = random.randint(1, N-1)
	g = 1
	while g==1:             
		x = ((x * x) % N + c) % N
		y = ((y * y) % N + c) % N
		y = ((y * y) % N + c) % N
		z = int(abs(x-y))
		N = int(N)
		g = gcd(z, N)
	return g
            
def primeFactorization(n):
    if n <= 0: raise ValueError("n <= 0")
    elif n == 1: return []
    queue = Queue()
    factors=[]
    queue.put(n)
    while(not queue.empty()):
        l=queue.get()
        if(miller(l)):
            factors.append(l)
            continue
        d=pollard_rho(l)
        if(d==l):queue.put(l)
        else:
            queue.put(d)
            queue.put(l/d)
    return factors

def product(n_list):
	n_set = set(n_list)
	result = 1
	for num in n_set:
		result *= int(num)
		
	return result

def maxval(d):
	#a) create a list of the dict's keys and values; 
	#b) return the key with the max value"""  
	v = list(d.values())
	k = list(d.keys())
	return v[v.index(max(v))]		
    
def rad():
	
	n = 1
	while True:
		yield n, product(primeFactorization(n))
		n += 1

vals = []
#Generate rads

for n, r in rad():
	item = (n, r)
	vals.append(item)
	
	#print(vals)
	sys.stdout.write("\rn = " + str(n))
	sys.stdout.flush()
	
	if n == 100000:
		break

new_list = sorted(vals, key=itemgetter(1))

print()
print("E(10000) = " + new_list[9999])


