#euler 36

import math

def pal(n_list):
	#number = list(str(n))
	number = n_list
	
	half = len(number) / 2	
	i = 0
	last = len(number) - 1
	
	
	
	if len(number) % 2 == 0:
		end = half
	else:
		end = math.floor(half)
	
	while i < end:
		if number[i] == number[last]:
			i += 1
			last -= 1
		else:
			return False
	return True
	
def dec_to_bin(n):
	if n == 0:
		return [0]
	
	elif n == 1:
		return [1]
	
	bin_dig = []
	
	dividend = n
	
	
	while dividend != 0:
		
		quotient = dividend//2
		remainder = dividend - (2 * quotient) 
		bin_dig.append(remainder)
		
		dividend = quotient
	
	bin_dig.reverse()

	return bin_dig

result = 0
		
for i in range(0, 1000000):
	dig_list = list(str(i))
	if pal(dig_list):
		if pal(dec_to_bin(i)):
			result += i
			print(i)
			
print("Final result: " + str(result)) 
		
		