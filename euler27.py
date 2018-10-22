#euler 27

import math




def calc_primes(n):	

	#0 mean not prime
	#1 means prime
	bools = [0, 0]
	primes = []

	for i in range(2, n):
		bools.append(1)

	t = 2
	sum = 0
	working = True
	current_prime_index = 2

	while working:
		#print("Next prime: " + str(t))
		j = t
		primes.append(t)
		sum += t
	
		#set all multiple of t to 0
		while j < len(bools):
			j += t
			try:
				bools[j] = 0
			except:
				pass
			
		#Set the next prime to the first number in the list that is not zero
		k = t + 1
		still_looking = True
		while still_looking:
			#print("Testing bools[" + str(k) + "] = " + str(bools[k]))
			try:
				if bools[k] == 1:
					t = k
					still_looking = False
				k += 1
			except:
				return primes
			
plist = calc_primes(10000)

a = -1000
b = -1000

results1 = []
results2 = []

#i = 0
#b = plist[i]

#a = -79
#b = 1601

highest_overall = 0

while a < 1000:
	#print("a = " + str(a))
	#print("Entering a loop, a = " + str(a))
	failed = False
	i = 0
	b = plist[i]
	while b <= 1000:
		#print("Entering b loop, b = " + str(b))	
		n = 0
		highest = 0
		
		while not failed:
			#print("a = " + str(a) + ", b = " + str(b) + " N = " + str(n))
			value = (n*n) + (n*a) + b
			#print("Value = " + str(value))
			if value not in plist:
				failed = True
				#print(str(value) + " is not in plist, moving to next b value and resetting n to 0")
				#print("n^2 + " + str(a) + "n + " + str(b))
				#print("Highest prime value when n = " + str(n) + " which is " + str(highest))
				
				
			else:
				#print(str(value) + " IS in plist, trying next n value")
				highest += 1
				n += 1
				
				#print("n^2 + " + str(a) + "n + " + str(b) + " = " + str(value))
				#input()
			
			
		
		if highest > 0:
			if highest > highest_overall:
				highest_overall = highest
				high_a = a
				high_b = b

			#print("Saving highest = " + str(highest))
			
		
		i += 1
		b = plist[i]
		#b += 1
		failed = False
	a += 1
	#i = 0
	
print("Results")
print("Greatest number of consecutive primes: " + str(highest_overall))	
print("a = " + high_a + ", b = " + high_b + ", a x b = " + str(high_a * high_b))

		
	
	