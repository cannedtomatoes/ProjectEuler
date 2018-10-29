#euler 56

def sum_digs(n):
	n_list = list(str(n))
	n_list_ints = []
	
	for i in n_list:
		n_list_ints.append(int(i))
 
	return sum(n_list_ints)	
		
highest = 0		
		
for a in range(0, 100):
	for b in range(0, 100):
		power = a**b
		#print(str(a) + "^" + str(b) + " = " + str(power))
		digit_sum = sum_digs(power)
		if digit_sum > highest:
			highest = digit_sum
			
print(highest)