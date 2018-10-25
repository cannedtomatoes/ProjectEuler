#euler 45

import math

def t(n):
	return (n*(n+1)/2)

#def n_t(n):
#	return (-1+math.sqrt(1+(8*n)))/2
	
def p(n):
	return (n*((3*n)-1)/2)

#def n_p(n):
#	return (1+math.sqrt(1+(24*n)))/6
	
def h(n):
	return n*((2*n)-1)

#def n_h(n):
#	return (1+math.sqrt(1+(8*n)))/4
	
found = False



# Generate all triangular, pentagonal and hexagonal numbers with odd n values
# Choose T_n with n > 285
# Compare T to P with all n < 285
# If matched, compare with H with n < 285


tris = []
pents = []
hects = []

for i in range(1, 1000000, 2):
	tris.append(t(i))
	pents.append(p(i))
	hects.append(h(i))

print("Searching...")

i = 0
while not found:
	tri = tris[i]
	
	for j in range(0, i):
		if tri == pents[j]:
			pent = pents[j]
			
			for k in range(0, j):
				if hects[k] == pent:
					 print("Found solution with Tn = " + str(tri))
					 exit()
					 
	i += 1
