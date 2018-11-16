#euler 69
#relatively prime - no common factors other than 1

from tqdm import tqdm
from math import gcd
import random
from queue import Queue

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

def phi(n):

    if miller(n): return n-1
    phi = n
    for p in set(primeFactorization(n)):
        phi -= (phi/p)
    return phi

def quotient(n):
	#try:
	return n/phi(n)
	#except:
	#	return None

def phi_and_n_are_perms(num):
	p = phi(num)
	p_list = list(str(int(p)))
	n_list = list(str(int(num)))
	p_list = sorted(p_list)
	n_list = sorted(n_list)
	
	#print("p_list: " + str(p_list) + ", n_list: " + str(n_list))
	
	return p_list == n_list


	
limit = (10**7) + 1
min_q = 10000000000000	
min_n = 0
	
for i in range(2, limit):
	#print("i = " + str(i))

	if phi_and_n_are_perms(i):

		q = quotient(i)
		#print("q = " + str(q) + " when n = " + str(i))
		if q < min_q:
			print("q = " + str(q) + " when n = " + str(i))
			min_q = q
			min_n = i
	
	
print("\nMIN VALS\nn= " +str(min_n) + ", q = " + str(min_q))