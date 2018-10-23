#euler33

def common_factor(n, d):
	#fraction is less than 1 so smaller number will be on the denominator
	factor = n
	while factor > 0:
		if d % factor == 0:
			return factor
		else:
			factor -= 1
	return None

def cancel_digit(num, den):
	
	num_list = list(str(num))
	den_list = list(str(den))
	
	if num_list[0] == den_list[0] and num_list[0] != '0' and den_list[0] != '0':
		new_num = num_list[1]
		new_den = den_list[1]
		
	elif num_list[0] == den_list[1] and num_list[0] != '0' and den_list[0] != '0':
		new_num = num_list[1]
		new_den = den_list[0]
		
	elif num_list[1] == den_list[1] and num_list[1] != '0' and den_list[1] != '0':
		new_num = num_list[0]
		new_den = den_list[0]
		
	elif num_list[1] == den_list[0] and num_list[1] != '0' and den_list[1] != '0':
		new_num = num_list[0]
		new_den = den_list[1]
	else:
		new_num = num
		new_den = den
		
	if new_den != 0:
		return int(new_num), int(new_den)
	else:
		return num, den
		#print("Nothing equal, returning original")

lowest = 10
highest = 100
prod_num = 1
prod_den = 1

for i in range(lowest, highest):
	for j in range(lowest, highest):
	
		#print(str(i) + "/" + str(j))
		
		if i != j:
			
			if not (i % 10 == 0 and j % 10 == 0):
				
				actual_val = i/j
			
				n_num, n_den = cancel_digit(i, j)
				if n_den != 0 and n_num != i and n_den != j:
					new_val = n_num/n_den

					if actual_val == new_val and new_val < 1:
						#print("Winner!!")
						print(str(i) + "/" + str(j) + " = " + str(n_num) + "/" + str(n_den))
						prod_num *= n_num
						prod_den *= n_den

cf = common_factor(prod_num, prod_den)
prod_num = int(prod_num/cf)
prod_den = int(prod_den/cf)
		
print(str(prod_num) + "/" + str(prod_den))
			
		