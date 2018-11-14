#euler 64

#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

import math
from tqdm import tqdm

def pattern(n):
	
	digits = []

	a0 = math.floor(math.sqrt(n))
	#digits.append(a0)
	#print("n = " + str(n))
	#print("a0 = " + str(a0))

	d = 1
	m = 0
	a = a0
	i = 1
	
	while True:
	
		m_prev = m
		d_prev = d
		
		m = (d_prev*a) - m_prev
		d = (n - (m**2))/d_prev
		
		a = math.floor((a0 + m)/d)
		digits.append(a)
		
		#print("a" + str(i) + " = " + str(a))
	
		if a == 2*a0:
			#print(digits)
			return digits
	
		i += 1


squares = []
for j in range(1, 101):
	squares.append(j**2)
	
	
count = 0


		
for i in tqdm(range(1, 10001)):
	if i not in squares: 
		p = pattern(i)
		if len(p) % 2 != 0:
			count += 1

print(count)