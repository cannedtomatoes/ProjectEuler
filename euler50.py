#euler50

import math

def calc_primes(n):	

	#returns all primes less than n

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
				
plist = calc_primes(1000000)


start = 0
end = 1
highest = 0
highest_p = 0

while start < len(plist):
	#print("Start = " + str(start))
	end = start + 1
	while end < len(plist):

		total = 0
		current = start
	
		while current < end:
			
			#print("Start: " + str(start) + ", end: " + str(end))
			
			total += plist[current]
			#print("Current total = " + str(total))
		
			current += 1

		
		if total in plist:
			#print(str(total) + " is the sum of " + str(end-start) + " primes. S = " + str(start) + ", E = " + str(end))
			
			if (end-start) > highest:
				highest = (end-start)
				highest_p = total
				print(str(total) + " is the sum of " + str(end-start) + " primes. S = " + str(start) + ", E = " + str(end))
			
		if total > 1000000:
				break

		end += 1
	start += 1
	
print("P = " + str(highest_p) + ", C = " + str(highest))
	