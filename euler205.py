#euler205

import random
import sys
import itertools
from fractions import Fraction 

peter = [1, 2, 3, 4] #9
colin = [1, 2, 3, 4, 5, 6] #6

prob = (Fraction(1, 4) ** 9) * (Fraction(1,6) ** 6)
output = 0
count = 0

for p in itertools.product(peter, repeat=9):

    p_sum = sum(p)
    count += 1
    
    sys.stdout.write("\r" + str(count))
    sys.stdout.flush()

    for c in itertools.product(colin, repeat=6):
        
        c_sum = sum(c)
        
        if p_sum > c_sum:
            
            output += prob

    
    #sys.stdout.write("\r" + str(output.numerator / output.denominator))
    #sys.stdout.flush()
    
print(output)
print(str(output.numerator / output.denominator))