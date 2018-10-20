#euler 21

import math

#Does not return the number itself
def factors(n):
	
	if n == 1:
		return [1]
	
	r = []
	i = 1
	while i < math.sqrt(n):
	
		if n % i == 0:
			r.append(i)
			if i != n and i != 1: #remove the and etc to make it normal
				r.append(int(n/i))
		i += 1
	return r
	
def get_sum(n):

	return sum(factors(n))
		
# while True:
	# inp = int(input("> "))
	# print(get_sum(inp))

# get_sum(i = 220) = 284 one	
# get_sum(one 284) = 220 two

results = []
	
for i in range(10001):
	one = get_sum(i)
	two = get_sum(one)
	
	if two == i and one != i:
		
		if one not in results:
			results.append(one)
			results.append(two)
			
print(sum(results))