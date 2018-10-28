#euler 53

def factorial(num):
	output = 1
	for i in range(1, num+1):
		output *= i
		
	return output
	
def ncr(n, r):
	return factorial(n) / (factorial(r)*factorial(n-r))
	
result = 0	
	
for n in range(1, 101):
	for r in range(1, 101):
		if ncr(n, r) > 1000000:
			result += 1
			
print(result)