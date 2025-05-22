#euler 174

import sys
from sympy import divisors

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


def same(val1, val2):
    
    if val1 % 2 == 1:
        
        if val2 % 2 == 1:
            
            return True
    else:
        if val2 % 2 != 1:
            
            return True
            
    return False




result = 0

for T in range(1, 1000001):

    sys.stdout.write("\r" + str(T))
    sys.stdout.flush()
    
    this_result = 0


    for f in find_factor_pairs(T):

        S1 = (f[1] + f[0])/2
    
        S2 = f[1] - S1
    
        if S1 > 0 and S2 > 0 and S1 > S2:
    
            if S1.is_integer() and S2.is_integer():
            
                if same(S1, S2):
    
                    this_result += 1
              
                
    if 1 <= this_result <= 10:
    
        result += 1
        #print(T)

print()
print(result)
    
    
