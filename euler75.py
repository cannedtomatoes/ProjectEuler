#euler 75

import math
from tqdm import tqdm
import sys
from collections import Counter

def count_one(result, results_list):
	found = False
	for r in results_list:
		if r == result:
			if found:
				return False
			else:
				found = True
				
	
	return True

			


found = []
count = 0


for m in range(1, 1000):
		for n in range(1, 1000):
			
			sys.stdout.write("\r" + str(count) + " primitives checked")
			sys.stdout.flush()
			if m > n:
				both_odd = (m % 2 != 0) and (n % 2 != 0)
				if not both_odd:
					if math.gcd(m,n) == 1:
						count += 1
						#primitive
						a = m**2 - n**2
						b = 2*m*n
						c = m**2 + n**2
						
						a1 = a
						b1 = b
						c1 = c
						
						k = 1
						
						while (a1 + b1 + c1) <= 1500000:
							a1 = a * k
							b1 = b * k
							c1 = c * k
							
							length = a1 + b1 + c1
							if length < 1500000:
								found.append(length)
							
							k += 1

								
						
confirmed = []

print("\nChecking " + str(len(found)) + " results...")

c = Counter(found)
							
for L in found:

	if c[L] == 1:
		confirmed.append(L)
							
print("Total: " + str(len(confirmed)))
