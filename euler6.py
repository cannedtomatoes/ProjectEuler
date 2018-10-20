#euler6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


sum1 = 0
sum2 = 0

for i in range(1, 101):
	sum1 += (i * i)
	sum2 += i

sum2 = (sum2 * sum2)	
	
print(str(sum2 - sum1))