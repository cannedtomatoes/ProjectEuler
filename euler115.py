#euler 115

import sys

def f(n, m, d):
    
    if n in d:
        return d[n]
    
    if n < m:
    
        return 1
    else:
    
        count = 0
        
        #first piece is black square
        
        count += f(n-1, m, d)
        
        #red block uses up m units
        
        for p in range(m, n+1):
        
            #sys.stdout.write("\r" + "    " + str(count) + "    ")
            #sys.stdout.flush()
            
            #if there is any space left after adding the red block
            if n - p - 1 < 0:
            
                count += 1
                
            else:
                
                count += f((n - p - 1), m, d)
        
        d[n] = count
        return count

#N = int(input("> "))
d = {}

total = 0

limit = 1_000_000

M = 50

N = 3

while True:

    total = f(N, M, d)

    sys.stdout.write("\r" + "n = " + str(N) + ", total = " + str(total))
    sys.stdout.flush()

    if total > limit:
        break
    else:
        N += 1
