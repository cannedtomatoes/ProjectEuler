#euler41

import math
from tqdm import tqdm

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
		
def pandigital(n):
	big_list = list(str(n))
	length = len(big_list)
	all_numbers = sorted(big_list)

	all_numbers_str = ''.join(all_numbers)
	#print(all_numbers_str)

	test = '123456789'
	
	if all_numbers_str == test[:length]:
		return True
	else:
		return False
		
largest = 0
pan_nums = []
for i in tqdm(range(1, 987654322)):
	
	if pandigital(i):
		
		pan_nums.append(i)
		
for j in tqdm(pan_nums):
	if is_prime(j):
		if j > largest:
			largest = j
				
print("Solution: " + str(largest))