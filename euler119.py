#euler 119


def dig_sum(n):
	num_list = list(str(n))
	output = 0
	
	for d in num_list:
		output += int(d)
	
	return output
	
	
	


i = 1
results = []

for base in range(2, 100): 
	
	#sys.stdout.write("\rTesting " + str(base) + "^" + str(i))
	#sys.stdout.flush()
	
	
	
	for i in range(1, 100):
		
		#print("Testing " + str(base) + "^" + str(i))
		
		result = base**i
		#if result < 10:
		#	break
		
		if base == dig_sum(result):
			
			#print("\n" + str(base) + "^" + str(i) + " = " + str(result))
			#input()
			results.append(result)
			
	
	base += 1
	
for e in enumerate(sorted(results), -7):
	print(e)