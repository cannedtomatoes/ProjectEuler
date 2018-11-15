#euler 65
#https://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems
#convergents h/k
# h_n = a_n x h_n-1 + h_n-2    h_-1 = 1    h_-2 0


def gen_e(n):
	#generates coefficients of continued fraction for e, with count n
	k = 1
	count = 0
	output = [2]
	
	while count < n:
		output.append(1)
		output.append(2*k)
		output.append(1)
		
		k += 1
		count += 1
	
	return output

coeffs = gen_e(1000)

hm1 = 1
hm2 = 0

for i in range(0, 100):

	hn = (coeffs[i] * hm1) + hm2 
	#print(hn)
	
	hm2 = hm1
	hm1 = hn

	
h = list(str(hn))
total = 0
for num in h:
	total += int(num)
	
print(total)






