#euler 348

import math
import sys
from tqdm import tqdm

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2
	
def is_cube(n):
    cube_root = n**(1./3.)
    return round(cube_root) ** 3 == n

def s_and_c(n_list):
	n1 = n_list[0]
	n2 = n_list[1]
	
	if is_square(n1):
		if is_cube(n2):
			return True
		else:
			return False
	elif is_cube(n1):
		if is_square(n2):
			return True
		else:
			return False
	else:
		return False
    
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

def gen_halves(n):
	halfway = math.ceil(n/2) + 1
	for i in range(2, halfway):
		yield (i, (n-i))
	
all_nums = {}

s_min = 2
s_max = 50000
c_min = 2
c_max = 25000

print("Generating numbers")

squares = []
for i in range(s_min, s_max + 1):
	squares.append(i*i)

cubes = []	
for j in range(c_min, c_max + 1):
	cubes.append(j*j*j)

print("Checking")

results = []
	
for s in tqdm(squares):
	
	for c in cubes:
		
		num = s + c
		if pal(num):
			
			if num not in all_nums:
				all_nums[num] = 1
			else:
				all_nums[num] += 1
				
				if all_nums[num] == 4:
					#print("Winner: " + str(num))
					results.append(num)
					
print(results)
print(sum(results))
		






