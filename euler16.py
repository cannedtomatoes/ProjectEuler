#euler16

num = 2**1000

num_l = list(str(num))

sum = 0

for n in num_l:
	sum += int(n)
	
print(sum)
