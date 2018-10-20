#euler10
#Find the sum of all the primes below two million.

from tqdm import tqdm
import math

def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2, int(math.sqrt(n))):
			print("n % i = " + str(n % i))
			if n % i == 0:
				return False
				
		return True

sum = 0
for j in range(2000000):
	print("Testing " + str(j))
	if is_prime(j):
		sum += j
		print("Adding " + str(j))
		
	if j == 10:
		input()

print(sum)