#euler68

import itertools

def all_equal(nums):
	first = nums[0]
	for n in nums:
		if n != first:
			return False
	return True

def totals(g):
	#end points in clockwise order
	ends = [0, 3, 5, 7, 9]
	sums = []
	
	#find lowest value
	low_val = 2000
	low_index = -1
	for e in ends:
		if g[e] < low_val:
			low_val = g[e]
			low_index = e
	
	if low_index == 0:
		sums.append(g[0] + g[1] + g[2])
		piece1 = str(g[0]) + str(g[1]) + str(g[2])
		sums.append(g[3] + g[2] + g[4])
		piece2 = str(g[3]) + str(g[2]) + str(g[4])
		sums.append(g[5] + g[4] + g[6])
		piece3 = str(g[5]) + str(g[4]) + str(g[6])
		sums.append(g[7] + g[6] + g[8])
		piece4 = str(g[7]) + str(g[6]) + str(g[8])
		sums.append(g[9] + g[8] + g[1])
		piece5 = str(g[9]) + str(g[8]) + str(g[1])
		
		solution = piece1 + piece2 + piece3 + piece4 + piece5
		
	elif low_index == 3:		
		
		sums.append(g[3] + g[2] + g[4])
		piece1 = str(g[3]) + str(g[2]) + str(g[4])
		sums.append(g[5] + g[4] + g[6])
		piece2 = str(g[5]) + str(g[4]) + str(g[6])
		sums.append(g[7] + g[6] + g[8])
		piece3 = str(g[7]) + str(g[6]) + str(g[8])
		sums.append(g[9] + g[8] + g[1])
		piece4 = str(g[9]) + str(g[8]) + str(g[1])
		sums.append(g[0] + g[1] + g[2])
		piece5 = str(g[0]) + str(g[1]) + str(g[2])
		
		solution = piece1 + piece2 + piece3 + piece4 + piece5
		
	elif low_index == 5:		
		
		sums.append(g[5] + g[4] + g[6])
		piece1 = str(g[5]) + str(g[4]) + str(g[6])
		sums.append(g[7] + g[6] + g[8])
		piece2 = str(g[7]) + str(g[6]) + str(g[8])
		sums.append(g[9] + g[8] + g[1])
		piece3 = str(g[9]) + str(g[8]) + str(g[1])
		sums.append(g[0] + g[1] + g[2])
		piece4 = str(g[0]) + str(g[1]) + str(g[2])
		sums.append(g[3] + g[2] + g[4])
		piece5 = str(g[3]) + str(g[2]) + str(g[4])
		
		solution = piece1 + piece2 + piece3 + piece4 + piece5
		
	elif low_index == 7:
		
		
		sums.append(g[7] + g[6] + g[8])
		piece1 = str(g[7]) + str(g[6]) + str(g[8])
		sums.append(g[9] + g[8] + g[1])
		piece2 = str(g[9]) + str(g[8]) + str(g[1])
		sums.append(g[0] + g[1] + g[2])
		piece3 = str(g[0]) + str(g[1]) + str(g[2])
		sums.append(g[3] + g[2] + g[4])
		piece4 = str(g[3]) + str(g[2]) + str(g[4])
		sums.append(g[5] + g[4] + g[6])
		piece5 = str(g[5]) + str(g[4]) + str(g[6])
		
		solution = piece1 + piece2 + piece3 + piece4 + piece5
		
	elif low_index == 9:
		
		
		sums.append(g[9] + g[8] + g[1])
		piece1 = str(g[9]) + str(g[8]) + str(g[1])
		sums.append(g[0] + g[1] + g[2])
		piece2 = str(g[0]) + str(g[1]) + str(g[2])
		sums.append(g[3] + g[2] + g[4])
		piece3 = str(g[3]) + str(g[2]) + str(g[4])
		sums.append(g[5] + g[4] + g[6])
		piece4 = str(g[5]) + str(g[4]) + str(g[6])
		sums.append(g[7] + g[6] + g[8])
		piece5 = str(g[7]) + str(g[6]) + str(g[8])
		
		solution = piece1 + piece2 + piece3 + piece4 + piece5
	
	if all_equal(sums):
		return solution
	else:
		return None
	

#graph = [4, 3, 2, 6, 1, 5]

#print(totals(graph))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

perms = itertools.permutations(digits)

high_total = 0

for p in perms:
	#p = [6, 5, 3, 10, 1, 9, 4, 8, 2, 7]
	t = totals(p)
	#print(t)
	#exit()
	
	if t:
		if len(t) == 16:
			t_num = int(t)
			#print(t_num)
			if t_num > high_total:
				high_total = t_num
			#print(high_total)
		#print("total = " + str(t))
		#print(max_string(t))

print("Highest: " + str(high_total))
	
	
	