#euler 231

from sympy import isprime
from sympy import factorint
import math

def hpf(num):

    facts = factorint(num)
    print(facts)
    
    return list(facts.items())[-1][0]

def gen_primes():

    n = 2
    
    while True:
    
        if isprime(n):
            yield n
            
        n += 1

def Lf(num):

    v = {}

    for p in gen_primes():
        
        L = math.floor(math.log(num, p))
        total = 0
            
        for i in range(1, L+1):
            
            total += math.floor(num/p**i)
        
        if total == 0:
            return v
        else:
            v[p] = total

def multiply(facts1, facts2):

    facts_list_1 = facts1.keys()
    facts_list_2 = facts2.keys()

    result = {}
    
    for f1 in facts_list_1:
    
        if f1 in facts_list_2:
        
            result[f1] = facts1[f1] + facts2[f1]
            
        else:
        
            result[f1] = facts1[f1]
    
    for f2 in facts_list_2:
    
        if f2 not in facts_list_1:
        
            result[f2] = facts2[f2]
            
    return result

def subtract(facts1, facts2):

    facts_list_1 = facts1.keys()
    facts_list_2 = facts2.keys()

    top_facts = {}
    bottom_facts = {}
    
    for f1 in facts_list_1:
    
        if f1 in facts_list_2:
            
            if facts1[f1] - facts2[f1] != 0:
                top_facts[f1] = facts1[f1] - facts2[f1]
            
        else:
        
            top_facts[f1] = facts1[f1]
            
    for f2 in facts_list_2:
    
        if f2 not in facts_list_1:
        
            bottom_facts[f2] = facts2[f2]
            
    return top_facts, bottom_facts

n = 20_000_000
r = 15_000_000

top = Lf(n)
bottom = multiply(Lf(r), Lf(n-r))

numerator, denominator = subtract(top, bottom)

print(numerator, denominator)

final_result = 0

for key, value in numerator.items():
    
    final_result += (key*value)
    
print(final_result)

