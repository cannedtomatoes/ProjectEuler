#euler12

import math

def triangle(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
		
	return sum

def factors(n):
	f = []
	
	i = 1
	while i <= math.sqrt(n):
		if n % i == 0:
			f.append(i)
			if i != int(n/i):
				f.append(int(n/i))
		i += 1
		
	return f


		
fact = []
j = 1

while True:
	num = triangle(j)
	fact = factors(num)
	
	#print(str(num) + " has " + str(len(fact)) + " factors: " + str(fact))
	#input()
	
	if len(fact) > 500:
		print("Result: " + str(num))
		exit()
	else:
		j += 1
	
	#input()