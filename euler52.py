#euler 52

def same_digits(n1, n2):
	n1_list = sorted(list(str(n1)))
	n2_list = sorted(list(str(n2)))
	
	return n1_list == n2_list
	
x = 1
found_solution = False
while not found_solution:
	if same_digits(x, (2*x)):
		if same_digits(x, (3*x)):
			if same_digits(x, (4*x)):
				if same_digits(x, (5*x)):
					if same_digits(x, (6*x)):
						found_solution = True
						print("Solution: " + str(x))
						exit()
	
	x += 1
	
