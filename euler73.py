#euler 73

def factorial(n):
	total = 1
	for i in range(1, n+1):
		total *= i
	return total

def next_fact(f):
	f_list = list(str(f))
	
	new_num = 0
	
	for digit in f_list:
		new_num += factorial(int(digit))
		
	return new_num

total = 0
	
for i in range(1000000):
	cycles = 0
	repeating = False

	num = i
	seen = [num]
	
	#print("Start number: " + str(i))
	
	while not repeating:
		num = next_fact(num)
		if num not in seen:
			seen.append(num)
		else:
			cycles = len(seen)
			if cycles == 60:
				total += 1
				print(i)
				print("Total: " + str(total))
			repeating = True
	
	