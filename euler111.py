import math
from collections import Counter
import sys

def simple_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def segmented_sieve(low, high, segment_size=10_000_000):
    """Yield primes in [low, high) in memory-efficient segments."""
    limit = int(math.isqrt(high)) + 1
    primes = simple_sieve(limit)

    for seg_low in range(low, high, segment_size):
        seg_high = min(seg_low + segment_size, high)
        sieve = [True] * (seg_high - seg_low)

        for p in primes:
            start = max(p*p, ((seg_low + p - 1) // p) * p)
            for multiple in range(start, seg_high, p):
                sieve[multiple - seg_low] = False

        for i, is_prime in enumerate(sieve):
            n = seg_low + i
            if is_prime and n >= 10**9:   # only yield 10-digit numbers
                yield n

# Example usage: process primes one by one
low = 10**9
high = 10**10

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

M = {}
N = {}
S = {}

total = 0

for digit in digits:

    M[digit] = -1
    N[digit] = 0


for prime in segmented_sieve(low, high):
    
    sys.stdout.write("\r" + str(prime) + "    ")
    sys.stdout.flush()
    
    c = Counter(str(prime))
    
    for digit in digits:
    
        if c[digit] > M[digit]:
        
            M[digit] = c[digit]
            #N[digit] = 0
            S[digit] = 0
            
        if c[digit] == M[digit]:
        
            #N[digit] += 1
            S[digit] += prime
            
       
for key, val in S.items():

    total += val
    
    
print()    
print(total)
