#euler29

import itertools

nums = range(2, 101)

perms = list(itertools.product(nums, repeat=2))

results = []

for p in perms:
	result = p[0]**p[1]
	#print(str(p[0]) + " x " + str(p[1]) + " = " + str(result))
	results.append(result)


	
print(len(set(results)))