#euler57
from fractions import Fraction

a = Fraction(5, 2)
output = 0
#iteration 1
result = Fraction(3, 2)
#print(result)
#iteration 2 and onwards
a = Fraction(1,2)
for n in range(2, 1001):
	
	a = Fraction(1, 2 + a)
	result = 1 + a
	#print(result)
	
	num = result.numerator
	den = result.denominator
	
	num_list = list(str(num))
	den_list = list(str(den))
	
	if len(num_list) > len(den_list):
		output += 1

print(output)