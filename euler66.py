#euler 66
#
#https://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems
#https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
#convergents h/k
# h_n = a_n x h_n-1 + h_n-2    h_-1 = 1    h_-2 0
# k_n = a_n x k_n-1 + k_n-2    k_-1 = 0    k_-2 1

#Assuming minimal solution for x is the smallest value of x that makes a true equation

import math

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
			return a0, digits
	
		i += 1
		
def gen_c(n, num):
	#Generates list of repeating coefficients of root n
	#num is how many to produce in total
	
	first, rep = pattern(n)
	times = math.ceil(num/len(rep))
	
	output = [first]
	for i in range(0, times-1):
		output.extend(rep)
		
	return output
	
def test_sol(n, x, y):
	#print(str(x) + "^2 - " + str(n) + " * " + str(y) + "^2 = 1")

	if ((x**2) - (n* (y**2))) == 1:
		return True
	else:
		return False

squares = []
for j in range(1, 101):
	squares.append(j**2)

big_x = 0
high_D = -1



for D in range(1, 1001):
	
	if D not in squares:
		
		#print("D = " + str(D))
		
		coeffs = gen_c(D, 100)

		x_found = False

		hm1 = 1
		hm2 = 0
		km1 = 0
		km2 = 1
		
		
		for a in coeffs:
			

			hn = (a * hm1) + hm2 
			kn = (a * km1) + km2
	
			hm2 = hm1
			hm1 = hn
	
			km2 = km1
			km1 = kn
			
			
			#print("x = " + str(hn))
			#print("y = " + str(kn))
			
			#print("Testing a = " + str(a) + " h/k = " + str(hn) + "/" + str(kn))
			if not x_found:
				if test_sol(D, hn, kn):

					x_found = True
					
					if hn > big_x:
						big_x = hn
						high_D = D
						
						print("D = " + str(high_D))
						print("x = " + str(big_x)) 
			
