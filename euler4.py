#euler4
#Find the largest palindrome made from the product of two 3-digit numbers.
# 100 * 100 = 10000
# 999 * 999 = 998001
# Hence we are looking for palindromic numbers between 10000 and 998001

import math

def pal(n):
	number = list(str(n))
	
	half = len(number) / 2	
	i = 0
	last = len(number) - 1
	
	
	
	if len(number) % 2 == 0:
		end = half
	else:
		end = math.floor(half)
	
	while i < end:
		if number[i] == number[last]:
			i += 1
			last -= 1
		else:
			return False
	return True


	
largest = 0
found = False
results = []	
	
for p1 in reversed(range(100, 1000)):
	for p2 in reversed(range(100, 1000)):
		
		result = p1 * p2
		#print(str(p1) + " x " + str(p2) + " = " + str(result))
		if pal(result):
			results.append(result)
			
print(max(results))


