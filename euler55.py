#euler 55

import math


def pal(n):
	number = list(str(n))
	#number = n_list
	
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
	
def digits_reversed(num):
	return int(''.join(reversed(list(str(num)))))
	
lychrels = 0

for i in range(1, 10000):
	
	c_num = i
	count = 0
	found = False
	
	while not found:
		
		if count == 50:
			lychrels += 1
			break	

		c_rev = digits_reversed(c_num)
		total = c_num + c_rev
		if pal(total):
			found = True
		else:
			c_num = total
			count += 1
			
print(lychrels)
	