#euler 49

import math
import itertools

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

def gen_primes():
	#n = 2
	n = 1000
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

seen = []
		
for p in gen_primes():
	if p not in seen:
		
		print("Test number: " + str(p))
		
		seen.append(p)
		
		prime_list = prime_list = list(str(p))
		
		perms = list(itertools.permutations(prime_list))
		
		all_primes = [p]

		
		#print("Permutations that are also prime:")
		for perm in perms:
			potential_prime = int(''.join(perm))
			if is_prime(potential_prime) and potential_prime > 1000 and potential_prime not in all_primes:
				all_primes.append(potential_prime)
		
		seen.extend(all_primes)
		#print(all_primes)
		
		if len(all_primes) > 2:
			
			#Test if there is a consistent gap between exactly three of the primes
			
			combs3 = list(itertools.combinations(all_primes, 3))
			
			for comb in combs3:
				if comb[1] - comb[0] == comb[2] - comb[1]:
					print("Found a winner!")
					print(comb)
					solution = []
					for c in comb:
						solution.append(str(c)) 
					print("Solution: " + ''.join(solution))
					input()
		
		

		
	