#Euler 5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_div(n):
	for i in range(2, 20):
		if n % i != 0:
			return False
			
	return True
	
k = 1

while True:
	num = 20 * k
	
	if is_div(num):
		print(num)
		exit()
	else:
		k += 1