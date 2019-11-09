#euler 203

import operator as op
from functools import reduce
import random
import sys
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

def sfree(n, psl):
	for ps in psl:
		if ps > n:
			last = ps
			break
		
	for ps in psl:
	
		if n % ps == 0:
			return False
	
	return True

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
	


print("Generating prime squares")

ps_list = []
num = 1

#f = open("prime_squares.txt")

#lines = f.readlines()

#for l in lines:
#	val = int(l.replace("\n", ""))
#	ps_list.append(val)
	

while num < 11243247:
	
	#per = int(100*num/15746723)
	sys.stdout.write("\r" + str(num) + "/15746723")
	#sys.stdout.write("\r" + str(per) + "%")
	sys.stdout.flush()

	if miller(num):
		num_sq = num*num
		ps_list.append(num_sq)

		
	num += 1
	
	
	
print("Generating combinations")		

c = []	
	
for i in range(1, 51):

	for j in range(1, i + 1):
	
		cf = int(ncr(i,j))
		
		if cf not in c:
			c.append(cf)
	
print("Performing analysis")

result = 0

for no in tqdm(c):
	if sfree(no, ps_list):
		result += no
		
print(result)