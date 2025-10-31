#euler 303

import sys
import itertools
from collections import deque

def doit2(n):

    queue = deque()
    visited = set()

    # enqueue initial possibilities (can’t start with 0)
    for d in [1, 2]:
        remainder = d % n
        queue.append((remainder, str(d)))
        visited.add(remainder)

    while queue:
        remainder, digits = queue.popleft()

        if remainder == 0:
            return digits   # Found number divisible by n

        for d in [0, 1, 2]:
            new_remainder = (remainder * 10 + d) % n

            if new_remainder not in visited:
                visited.add(new_remainder)
                queue.append((new_remainder, digits + str(d)))

def doit(n):

    digs = ['0', '1', '2']
    m = 1
    
    while True:

        

        for p in itertools.product(digs, repeat=m):
            
            if p[0] == '0':
                continue
            
            mult = int(''.join(p))
            #print(p, mult)
            
            if mult % n == 0:
                #print("Returning because", mult, "is a multiple of", n)
                return mult
        
        m += 1
            
limit = 10000
result = 0

for n in range(1, limit + 1):
    
    #print(n, doit(n))
    
    result += int(doit2(n))/n

    sys.stdout.write("\r" + str(n))
    sys.stdout.flush()

print()
print(result)

