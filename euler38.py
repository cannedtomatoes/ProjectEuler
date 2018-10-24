#euler 38

def pandigital(big_list):
	
	all_numbers = sorted(big_list)
	

	all_numbers_str = ''.join(all_numbers)
	#print(all_numbers_str)

	if all_numbers_str == '123456789':
		return True
	else:
		return False

def mult_pan(mult):
	digits = []
	n = 1
	
	while len(digits) <= 9:
		prod = mult * n
		#print(str(prod) + " = " + str(mult) + " x " + str(n))
		prod_str = str(prod)
		for p in prod_str:
			digits.append(p)
			#print(digits)
			
		if pandigital(digits):
			digits_str = ''.join(digits)

			return int(digits_str)
			
		else:
			n += 1
	

	return None

largest = 0
for i in range(100000):		
	result = mult_pan(i)	
	if result:
		print(result)
		if result > largest:
			largest = result

print("Final result: " + str(largest))	