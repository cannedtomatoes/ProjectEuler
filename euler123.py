#euler 123

import random
import sys

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
    
def gen_primes():
	N = 2
	while True:
		
		if miller(N):
			yield N
		
		N += 1

i = 1

for p in gen_primes():
	
	result = (((p - 1)**i) + ((p + 1)**i)) % (p**2)
	
	sys.stdout.write("\rr = " + str(result))
	sys.stdout.flush()
	
	#print("(p_" + str(i) + " - 1)^" + str(i) + " + (p_" + str(i) + " + 1)^" + str(i) + " / " + "(p_" + str(i) + ")^2 = " + str(result))
	#print("p = " + str(p))
	
	if result > (10**10):
		print("\n")
		print("n = " + str(i))
		exit()
		
	i += 1
	