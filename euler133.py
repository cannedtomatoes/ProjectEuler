#euler 133

from sympy import isprime
from sympy import factorint

def works(factors):
    
    truth_list = []
    
    for f in factors:
    
        truth_list.append(f in (2, 5))        
            
    return not all(truth_list)

def ord_p(p):

    test = 1
    
    while True:
    
        if pow(10, test, p) == 1:
        
            return test
            
        else:
        
            test += 1
    

def gen_primes(limit):

    output = []
    
    test = 7

    while test <= limit:

        if isprime(test):

            output.append(test)

        test += 1

    return output

def y_primes(limit):

    test = 7

    while test < limit:
    
        if isprime(test):

            yield test

        test += 1

count = 2 + 3 + 5  #account for 2, 3, 5

n = 1


for prime in y_primes(100000):

    op = ord_p(prime)
    
    facts = factorint(op).keys()
    
    #print(prime, works(facts), facts)
    #input()
    
    if works(facts):
        
        count += prime
            
print(count)
    
