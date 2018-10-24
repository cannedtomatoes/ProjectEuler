#euler 29


import math

def is_prime(n):
	if n < 2:
		return False
	else:
		i = 2
		while i <= math.sqrt(n):
			if n % i == 0:
				return False
			i += 1
				
		return True

def valid_ra_triangle(a, b, c):
	if c**2 == ((a**2) + (b**2)):
		return True
	else:
		return False

def triad(m):
	a = 2 * m
	b = (m**2) - 1
	c = (m**2) + 1
	
	return a, b, c
		
		
triads = [[3,4,5], [5,12,13], [7,24,25], [8,15,17], [9,40,41], [11,60,61], [12,35,37], [13,84,85], [15,112,113], [16,63,65], [17,144,145], [19,180,181], [20,99,101], [20,21,29], [	21,220,221], [23,264,265], [24,143,145], [25,312,313], [27,364,365], [28,195,197], [29,420,421], [31,480,481], [32,255,257], [33,544,545], [35,612,613], [36,323,325], [37,684,685], [39,760,761], [40,399,401], [41,840,841], [43,924,925], [44,483,485], [48,575,577]]


all_triangles = []

count = 0

for t in triads:
	a = 1
	b = 1
	c = 1
	n = 1
	count += 1
	#print("Count = " + str(count))
	while (a + b + c) < 1001:
		a = t[0] * n
		b = t[1] * n
		c = t[2] * n
		all_triangles.append([a,b,c])
		#print(str(a) + " " + str(b) + " " + str(c))
		n += 1

highest_num_of_solutions = 0

for k in range(3, 1000):

	solutions = 0
	
	for triangle in all_triangles:
		if sum(triangle) == k:
			solutions += 1
	
	if solutions > highest_num_of_solutions:
		print(str(k) + " is winning with " + str(solutions) + " solutions.")
		highest_num_of_solutions = solutions