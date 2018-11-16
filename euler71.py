#euler 71

# As the denominator increases, the fraction to the left follows a pattern
# where the numerator goes up by 3 and the denominator goes up by 7 so keep 
# doing that until the denomator hits 1000000

# I noticed this pattern when trying every value of n and d and finding the fraction
# wih the smallest difference from 3/7. As d increased every new fraction followed the pattern.

from fractions import Fraction

min_diff = Fraction(1,1)

g = Fraction(6422, 14985)



while g.denominator < 1000000:
	
	g = Fraction(g.numerator + 3, g.denominator + 7)
	diff = Fraction(3,7) - g
	
	if diff < min_diff:
		min_diff = diff
		print(g)
	