#euler47

import math

def convert(num_list):
	#Converts list of numbers so that if multiple primes exist,
	#they are multiplied together to form a single number
	
	seen = []
	new_list = []
	number_counts = {}
	
	#Count how many of each number there is
	for item in num_list:
		if item not in seen:
			number_counts[item] = num_list.count(item)
			seen.append(item)
			
	for key, value in number_counts.items():
		m = 1
		for i in range(1, value+1):
			m *= key
		new_list.append(m)
		
	return new_list

def all_distinct(big_list):
	seen = []
	
	for item in big_list:
		if item in seen:
			return False
		else:
			seen.append(item)
				
	return True 


def prime_factors(n): 
    
	p_facts = []
	  
	while n % 2 == 0: 
		p_facts.append(2) 
		n = n / 2
		  
	for i in range(3,int(math.sqrt(n))+1,2): 

		while n % i== 0: 
			p_facts.append(i) 
			n = int(n / i) 

	if n > 2: 
		p_facts.append(n) 

	return p_facts



t = 14
while t < 100000000:
	#print("Consdering " + str(t) + ", " + str(t+1) + " and " + str(t+2) + " and " + str(t+3))
	
	pfs = []
	
	pf1 = convert(prime_factors(t))
	pfs.extend(pf1)
	#print("pf1 = " + str(pf1))
	pf2 = convert(prime_factors(t+1))
	#print("pf2 = " + str(pf2))
	pfs.extend(pf2)
	pf3 = convert(prime_factors(t+2))
	#print("pf3 = " + str(pf3))
	pfs.extend(pf3)
	pf4 = convert(prime_factors(t+3))
	#print("pf4 = " + str(pf4))
	pfs.extend(pf4)
	
	#print("pfs = " + str(pfs))
	
	if all_distinct(pfs) and len(pf1) == 4 and len(pf2) == 4 and len(pf3) == 4 and len(pf4) == 4:
		print("Winner with values " + str(t) + ", " + str(t+1) + ", " + str(t+2) + ", and " + str(t+3))
		input()
	
	
	
	t += 1
	
