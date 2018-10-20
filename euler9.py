#euler 9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def is_triad(a, b, c):
	if ((a*a) + (b*b)) == (c*c):
		return True
	else:
		return False
		
for i in range(1, 1000):
	for j in range(1, 1000):
		for k in range(1, 1000):
			total = i + j + k
	
			if is_triad(i, j, k):
				print(str(i) + "^2 + " + str(j) + "^2 = " + str(k) + "^2")
				print("a + b + c = " + str(total))
				
				if total == 1000:
					print("WINNER")
					print("abc = " + str(i*j*k))
					exit()