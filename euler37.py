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

def trunc_left(n):
	
	
	temp = list(str(n))
	n_list = []
	
	for t in temp:
		n_list.append(int(t))
	
	output = []
	working = True
	
	while working:
		new_list = n_list[1:] #Slice off first element
		output.append(new_list)
		n_list = new_list
		length = len(n_list)
		
		if length < 2:
			working = False
	
	final = []		
	for o in output:
		temp = []
		for num in o:
			temp.append(str(num))
		final.append(int(''.join(temp)))
	
	return final
		
def trunc_right(n):
	temp = list(str(n))
	n_list = []
	
	for t in temp:
		n_list.append(int(t))
	
	output = []
	working = True
	
	while working:
		length = len(n_list)
		new_list = n_list[:(length-1)] #Slice off last element
		output.append(new_list)
		n_list = new_list
		length = len(n_list)
		
		if length < 2:
			working = False


	final = []		
	for o in output:
		temp = []
		for num in o:
			temp.append(str(num))
		final.append(int(''.join(temp)))
	
	return final

def truncs_both(number):
	for num in trunc_left(number):
		if is_prime(num) == False:
			return False

			
	for num in trunc_right(number):
		if is_prime(num) == False:
			return False

	return True

result = 0

for i in range(10, 1000000):
	if is_prime(i):
		
		#print(str(i) + " is prime.")

		if truncs_both(i):
			result += i
			print(i)
			
print("Final result: " + str(result))

				