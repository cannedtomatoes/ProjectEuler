#euler35

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

def all_prime(num_list):
	for num in num_list:
		if is_prime(num) == False:
			return False
	return True

def rotations(n):
	digits = list(str(n))
	output = []
	done = False
	
	current_num = digits
	
	while not done:
		new_num = []
		
		for i in range(1, (len(current_num))):
			new_num.append(current_num[i])
	
		new_num.append(current_num[0])
		number = int(''.join(new_num))
		if number not in output:
			output.append(number)
			current_num = new_num
		else:
			return output


# while True:
# 	u = int(input("> "))
# 	print(rotations(u))
result = 0
		
for j in range(2, 1000000):
	if is_prime(j):
		if all_prime(rotations(j)):
			result += 1
			print("Found solution: " + str(j))
				
print("Final result = " + str(result))
				
				