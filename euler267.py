#euler 267

import math
import sys

def prob(f):
    if f <= 0 or f >= 1:
        return 0.0
    
    improved = False

    #print(f)

    min_heads = (9 - (1000*math.log10(1-f))) / math.log10((1+(2*f))/(1-f))
    min_heads = math.ceil(min_heads)
    min_heads = max(0, min_heads)
    
    if min_heads > 1000 or min_heads < 0:
        return -1

    p = 0

    for heads in range(min_heads, 1001):

        p += math.comb(1000, heads) * ((0.5)**1000)
        
    return p



f = 0.1
highest_p = 0
best_f = 0
f_change = 0.05

while f_change > 1e-12:
    
    improved = False
    
    for direction in (-1,1):
    
        new_f = f + (direction*f_change)
    
        if 0 < new_f < 1:

            p = prob(new_f)
            
            if p == -1:
                continue
    
            if p > highest_p:
        
                highest_p = p
                best_f = new_f
                improved = True
    
    if improved:
    
        f = best_f
    
    else:
    
        f_change /= 2
    
    sys.stdout.write("\rf = " + str(f) + ", p = " + str(highest_p) + "  ")
    sys.stdout.flush()
