#euler34

def factorial(n):
	result = 1
	while n > 0:
		result *= n
		n -= 1
	return result

results = []
	
for i in range(3, 100000):
	total = 0
	num_str = list(str(i))
	
	for num in num_str:
		total += factorial(int(num))
		
	if i == total:
		print(str(i) + " is a winner")
		results.append(i)
		
print("\nSum of all results: " + str(sum(results)))