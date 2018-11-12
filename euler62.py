#euler62

import itertools

def largest_perm(n):
	output_list = []
	output = []
	
	num_list = list(str(n))
	num_list_ints = []
	
	for num in num_list:
		num_list_ints.append(int(num))
	
	while num_list_ints:	
		largest = max(num_list_ints)
		
		output_list.append(num_list_ints.pop(num_list_ints.index(largest)))
		
	for o in output_list:
		output.append(str(o))
		
	return int(''.join(output))


nums = {}
i = 345
found = False
all_cubes = []

j = 1
for j in range(1, 10000):
	all_cubes.append(j**3)


while not found:
	#print("Testing " + str(i) + "^3")
	cube = i**3
		
	largest_cube = largest_perm(cube)
	
	if largest_cube in nums:
		nums[largest_cube] += 1
		
		if nums[largest_cube] == 5:
			print("Found cube that appears 5 times:!")
			print(largest_cube)
			print("Calculating smallest radicand...")
			
			answer_list = list(str(largest_cube))
			answer_list.sort()
			

			perms = itertools.permutations(answer_list)
			for p in perms:
				
				if p[0] != '0':
				
					number = int(''.join(p))
					#print("Testing " + str(number))
				
					if number in all_cubes:
						rad = round(number ** (1/3))
						print("Answer: " + str(rad) + "^3 = " + str(number))
						exit()
					
			
			
		
	else:
		nums[largest_cube] = 1
	
	
	
	i += 1
		
