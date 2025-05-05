#euler 301

from functools import reduce
from operator import xor
import sys

limit = 2**30
output = 0
print(2**30)

for n in range(1, limit+1):

    sys.stdout.write("\r" + str(n))
    sys.stdout.flush()

    piles = [n, 2*n, 3*n]
    
    nim_sum = 0
    for pile in piles:
        nim_sum ^= pile
    
    if nim_sum == 0:
        output += 1

print()
print(output)
