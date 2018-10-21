#euler10
#Find the sum of all the primes below two million.

from tqdm import tqdm
import math

#0 mean not prime
#1 means prime
bools = [0, 0]
primes = []

#for i in range(2, 2000001):
#	bools.append(1)

for i in range(2, 2000001):
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
			#print(primes)
			print(sum)
			exit()
	
	
	