#euler 78
#https://en.wikipedia.org/wiki/Partition_function_(number_theory)
#https://brilliant.org/wiki/partition-of-an-integer/


n = 1
p = [1]

while True:
	i = 0
	pent = 1
	
	p.append(0)
	
	while pent <= n:
		if (i % 4) > 1:
			sign = -1
		else:
			sign = 1
			
		p[n] += int(sign * p[n - pent])
		p[n] = int(p[n] % 1000000)
		i += 1
		#print("n = " + str(n) + ", p[n] = " + str(p[n]))
		
		
		if i % 2 == 0:
			j = int((i / 2) + 1)
		else:
			j = int(-1 * ((i / 2) + 1))
		
		pent = int(j * ((3 * j) - 1) /2)
		
	if p[n] == 0:
		print("Winner!")
		print("n = " + str(n))
		exit()
		
	n += 1
	print(n)



# for k in gen_k():
# 	p = int((k * (3 * k) -1 )/2)
# 	print(str(n) + ": " + str(p))
# 	
# 	n += 1
# 	
# 	i