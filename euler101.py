#euler 101
#https://en.wikipedia.org/wiki/Lagrange_polynomial

from sympy import *


def product(list_of_exp):
	out = 1
	for e in list_of_exp:
		out *= e
	
	return out 

def other_vals(this_point, all_points):
	output = []
	for p in all_points:
		if p != this_point:
			output.append(p)
	
	return output
	
x = symbols("x")

#to sub
#expr.subs(x, 0)
FITs = []
x_list = []
real_terms = []
for n in range(1, 12):
	real_terms.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10)
	x_list.append(n)

#print(real_terms)
#print(x_list)

for i in range(1, 12):
	
	L = 0
	
	terms = real_terms[:i]
	xs = x_list[:i]
	
	#print("Considering x vals: " + str(xs))
	#print("Considering y vals: " + str(terms))
	
	if len(terms) == 1:
		L = terms[0]
		FITs.append(L)
		#print(L)
		#print("FIT: " + str(L))
	else:
		
		
		
		#Create l_i values of the form
		# x - x_m
		# -------
		# x_i - x_m
		
		# for m is the x for every point but this one.
		
		k = 0
		while k < len(xs):
		
			l = []
			for v in other_vals(xs[k], xs):
				frac = (x - v) / (xs[k] - v)
				l.append(frac)
				
			L += product(l)*terms[k]
			
			k += 1
			
		#print(L)
		
		#Generate FIT
		xf = x_list[len(xs)]
		y = L.subs(x, xf)
		FITs.append(y)
		#print("FIT: " + str(y))
		all_fits = sum(FITs)
		print(all_fits)
		input()