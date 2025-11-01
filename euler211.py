#euler 211

import sys
import math

def is_square(n):
    r = math.isqrt(n)
    return r * r == n
    
def divisor_square_sums(limit):
    divs = [1] * (limit + 1)
    for i in range(2, limit // 2 + 1):
        for j in range(i * 2, limit + 1, i):
            divs[j] += (i*i)
            
    for i in range(1, limit + 1):
        divs[i] += i * i
    return divs

print("Generating divisors...")
d = divisor_square_sums(64_000_000-1)
total = 1 # account for n=1 which is skipped
print("Done.")

for n, s in enumerate(d):
    
    if is_square(s):
    
        total += n


    sys.stdout.write("\r" + "n = " + str(n) + ", total = " + str(total))
    sys.stdout.flush()
