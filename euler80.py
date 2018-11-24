#euler 80

from decimal import *

getcontext().prec = 200

squares = []
total = 0

for j in range(1, 10):
	squares.append(j**2)

for n in range(1, 100):
	if n not in squares:
		
		

		t = list(str(Decimal(n).sqrt()))

		t.remove('.')



		for i in range(0, 100):
			total += int(t[i])
	
print(total)