#euler20
#Find the sum of the digits in the number 100!

def factorial(n):
	
	result = 1
	for i in reversed(range(1, n+1)):
		result *= i
		
	return result
	
f = factorial(100)

f_l = list(str(f))

result = 0

for num in f_l:
	result += int(num)
	
print(result)