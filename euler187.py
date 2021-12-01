#euler 187

import sys
from collections import Counter


#The previous version of this code created a list of all primes below (1x10^8 /2)
f = open("primes.txt")


lines_tmp = f.readlines()
nums = []
total = 0

c = Counter()

for l in lines_tmp:

	nums.append(int(l.strip()))

for n1 in nums:

	for n2 in nums:
	
		num = n1 * n2
		
		c[num] += 1
		
		if num <= 100000000:
		
			
			
		
			
			if c[num] < 2:
				#print(str(n1) + " x " + str(n2) + " = " + str(num))
				total += 1
			
			sys.stdout.write('\r' + str(total))
			sys.stdout.flush()
			
		else:
			break

print("\n\n")			

print(total)





	