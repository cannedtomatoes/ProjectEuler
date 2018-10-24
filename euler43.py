#euler 43

import math
from tqdm import tqdm
import itertools

def list_to_int(num_list):
	num_str = ''.join(num_list)
	return int(num_str)

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

def test_pan(pand, test_primes):
	#Test if pandigital has prescribed property
	
	m = 1
	n = 4
	for i in range(0, 7):
		pan_slice = pand[m:n]
		pan_slice_int = int(''.join(pan_slice))
		
		if pan_slice_int % test_primes[i] != 0:
			return False
		else:
			m += 1
			n += 1
	
	return True

primes = []
for p in gen_primes():
	primes.append(p)
	if p == 17:
		break

pans = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

perms = list(itertools.permutations(digits))
for perm in perms:
	if perm[0] != '0':
		pans.append(perm)

total = 0
		
for pan in tqdm(pans):
	if test_pan(pan, primes):
		total += list_to_int(pan)
		
print("Result: " + str(total))
		
