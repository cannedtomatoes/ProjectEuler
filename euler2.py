#Euler 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fibs = [1, 1]
sum = 0
num1 = 1
num2 = 1
new = 0

while num1 < 4000000:
	new = num1 + num2
	fibs.append(new)
	
	num1 = num2
	num2 = new

for f in fibs:
	if f % 2 == 0 and f < 4000000:
		sum += f
		
print(sum)