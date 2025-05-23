#euler 136

from sympy import divisors
import math
import sys

def find_factor_pairs(n):
    """
    Finds all pairs of factors for a given number.

    Args:
        n: The number for which to find factor pairs.

    Returns:
        A list of tuples, where each tuple represents a pair of factors.
    """

    factors = divisors(n)
    factor_pairs = []
    
    # Iterate through the factors and create pairs
    for i in range(len(factors)):
        factor_1 = factors[i]
        factor_2 = n // factor_1
        if (factor_1, factor_2) not in factor_pairs and factor_1 <= factor_2:
            factor_pairs.append((factor_1, factor_2))
    
    return factor_pairs

n = 0
total = 0

while n < 50000000:

    #print("n =", n)
    
    facts = find_factor_pairs(n)
    x_vals = []

    for f in facts:

        d = (f[0]+f[1])/4

        if d.is_integer():
        
            x1 = ((6*d) + math.sqrt((16*(d*d))-(4*n)))/2
            x2 = ((6*d) - math.sqrt((16*(d*d))-(4*n)))/2

            if x1 - (2*d) > 0:
                x_vals.append(x1)
                #print(d, x1)

            if x2 - (2*d) > 0 and x1 != x2:
                x_vals.append(x2)
                #print(d,  x2)
        
        

    if len(x_vals) == 1:

        total += 1
        #print(n, total)
        sys.stdout.write("\r" + str(n) + " "+ str(total))
        sys.stdout.flush()
        
    n += 1
    #input()
    
print()
print(total)
