#euler3
#What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(n):
	if n < 2:
		return False
	else:
		i = 2
		while i < n:
			if n % i == 0:
				return False
			i += 1
		return True
		
j = 1
largest = 0
while j < math.sqrt(600851475143):
	if 600851475143 % j == 0:
		if is_prime(j):
			if j > largest:
				largest = j
	j += 1
	
print(largest)