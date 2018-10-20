#euler7
#What is the 10 001st prime number?

import math

def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
				
		return True

count = 0
j = 1		
while j < 9223372036854775807:
	if is_prime(j):
		count += 1
		if count == 10001:
			print(j)
			exit()
	j += 1