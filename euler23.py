#euler23

import math
from tqdm import tqdm

#Does not return the number itself
def factors(n1):
	
	if n1 == 1:
		return [1]
	
	r = []
	k = 1
	while k <= math.ceil(math.sqrt(n1)):
	
		if n1 % k == 0:
			if k != n1:
				r.append(k)
			if k != n1 and k != 1: #remove the and etc to make it normal
				r.append(int(n1/k))
		
		if k**2 == n1:
			r.remove(k)
		
		k += 1
		
		 
	#print(str(n1) + " has factors " + str(r))	
	return list(set(r))

def is_a_n(n2):
	#print("Sum of factors of " + str(n2) + " = " + str(sum(factors(n2))))
	if sum(factors(n2)) > n2:
		return True
	else:
		return False

def sucess(n):
	for j in range(n):
		#print("Looking at possible sum: " + str(j) + " + " + str(n - j))
		if is_a_n(j):
			#print(str(j) + " is an abundant number...")
			if is_a_n(n - j):
				#print(str(j) + " + " + str(n-j) + " works (" + str(n) + ")")
				return True
	
	return False
		
results = []


		
for i in tqdm(range(1, 28124)):
	#print("Considering " + str(i))
	if sucess(i) == False:
		results.append(i)
		#print("Found value: " + str(i) )
		
		
print(sum(results))
	