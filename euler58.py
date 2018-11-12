#euler 58

import random
import math

def miller(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
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

#Read primes list
#f = open("P.txt")

#lines = f.readlines()
#f.close()

#prime_ref = []
#for line in lines:
#	l = line.split(", ")
#	prime_ref.append(int(l[1]))
	#print(l[1])
	

#grid = {}
	
#Grid dimension increase by 2 each iteration, ie 1^2, 3^2, 5^2, 7^2 etc...
	
size = 3
i = 1
# Centre number is the origin
x = 0
y = 0

done = False
checked = 0
primes_found = 0

#grid[(x,y)] = i
i += 1
#print(str(x) + ", " + str(y))
while not done:
	#print(size)
	#print("Going one to the right")
	#Move point one unit to the right
	x +=1
	#grid[(x,y)] = i
	if abs(x) == abs(y):
			checked += 1
			if i in prime_ref:
				primes_found += 1
	i +=1 
	#print(str(x) + ", " + str(y) + ": " + str(grid[(x,y)]))	
	
	#Move point size units up, creating a point each time
	
	#print("Going up")
	temp_y = y
	while y < (temp_y + size - 2):
		#print("Loop 1: while " + str(y) + " < " + str(y + size))
		y += 1
		#grid[(x,y)] = i
		if abs(x) == abs(y):
			checked += 1
			#if i in prime_ref:
			if miller(i):
				primes_found += 1
		#print(str(x) + ", " + str(y) + ": " + str(grid[(x,y)]))

		i += 1
		
	#print("Going left")
	#Move point size+1 units left, creating a point each time
	temp_x = x
	while x > (temp_x - (size-1) ):
		x -= 1
		#grid[(x,y)] = i
		if abs(x) == abs(y):
			checked += 1
			#if i in prime_ref:
			if miller(i):
				primes_found += 1
		i += 1
		#print(str(x) + ", " + str(y) + ": " + str(grid[(x,y)]))

	#print("Going down")
	#Move a point size+1 units down, creating a point each time
	temp_y = y
	while y > (temp_y - (size-1)):
		y -= 1
		#grid[(x,y)] = i
		if abs(x) == abs(y):
			checked += 1
			#if i in prime_ref:
			if miller(i):
				primes_found += 1
		i += 1	
	#	print(str(x) + ", " + str(y) + ": " + str(grid[(x,y)]))
	
	#print("Going right")
	#print("while " + str(x) + " < " + str(temp_x + size + 1))
	#Move point size+1 units right, creating a point each time
	temp_x = x
	while x < (temp_x + (size - 1)):
		x += 1
		#grid[(x,y)] = i
		if abs(x) == abs(y):
			checked += 1
			#if i in prime_ref:
			if miller(i):
				primes_found += 1
		i += 1	
		#print(str(x) + ", " + str(y) + ": " + str(grid[(x,y)]))

	
	
	rate = primes_found/checked
	#print(str(primes_found) + "/" + str(checked))
	print(str(rate))
	
	if rate < 0.1:
		print("Size: " + str(size-2))
		done = True
	
	
	size += 2