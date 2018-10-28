#euler46

import math

def gen_primes():
	n = 2
	while True:
		i = 2
		failed = False
		while i <= math.sqrt(n):
			if n % i == 0:
				failed = True
			i += 1
		
		if not failed:
			yield n	
			
		n += 1

def is_prime(n):
	if n < 2:
		return False
	else:
		i = 2
		while i <= math.sqrt(n):
			if n % i == 0:
				return False
			i += 1
				
		return True
		
def factors(n):
	i = 1
	output = []
	while i <= math.sqrt(n):
		if n % i == 0:
			output.append(i)
			if i != int(n/i):
				output.append(int(n/i))
		i += 1
	return output

def is_odd_comp(n):
	if n % 2 != 0 and not is_prime(n):
		return True
	else:
		return False
	
primes = []
count = 0
for p in gen_primes():
	primes.append(p)
	if count == 10000:
		break
	else:
		count += 1

squares = []
for s in range(1, 10000):
	squares.append(s**2)

	
still_working = True
c = 9

found_value = False
while still_working:
	while not is_odd_comp(c):
		c += 1
	i = 0
	prime = primes[i]
	while prime < c and found_value == False:
		#print("In while loop 1 with prime = " + str(prime))
		j = 0
		square = squares[j]
		while square < c and found_value == False:	
			#print("In while loop 2 with square = " + str(square))
			test = prime + (2 * square)
			#print("Testing " + str(prime) + " + 2 x " + str(square))
			if test == c:
				print(str(c) + " confirmed")
				found_value = True
			j += 1
			square = squares[j]
			
		i += 1
		prime = primes[i]
	

	
	if found_value == False:
		print(str(c) + " FAILED")
		still_working = False
	else:
		found_value = False
	c += 1	
	
	#input()
	
	
	