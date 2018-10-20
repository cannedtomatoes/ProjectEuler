#euler 24.py

import itertools

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = []

perms = list(itertools.permutations(n))

for p in perms:
	#print(p)
	temp = []
	q = list(p)
	for number in q:
		temp.append(str(number))
	nums.append(int(''.join(temp)))
	
nums_sorted = sorted(nums)

print(nums_sorted[999999])