#euler 32

import itertools
import math

def fact_pairs(n):
	
	output = []
	
	i = 1
	
	while i < math.ceil(math.sqrt(n)):
		if n % i == 0:
			f2 = int(n/i)
			output.append([i, f2])
			
		i += 1
			
	return output
		
def pandigital(one, two, three):
	
	all_numbers = []
	all_numbers.extend(list(str(one)))
	all_numbers.extend(list(str(two)))
	all_numbers.extend(list(str(three)))
	
	all_numbers.sort()
	all_numbers_str = ''.join(all_numbers)
	#print(all_numbers_str)

	if all_numbers_str == '123456789':
		return True
	else:
		return False

result = 0
seen = []

for j in range(1, 10000):
	for p in fact_pairs(j):
		if pandigital(p[0], p[1], j) and j not in seen:
			print(str(p[0]) + " x " + str(p[1]) + " = " + str(j))
			result += j
			seen.append(j)
			
print(result)