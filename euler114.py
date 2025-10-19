#euler 114

import sys

def f(n, d):
    
    if n in d:
        return d[n]
    
    if n < 3:
    
        return 1
    else:
    
        count = 0
        
        #first piece is black square
        
        count += f(n-1, d)
        
        #red block uses up m units
        
        for m in range(3, n+1):
        
            #sys.stdout.write("\r" + "    " + str(count) + "    ")
            #sys.stdout.flush()
            
            #if there is any space left after adding the red block
            if n - m - 1 < 0:
            
                count += 1
                
            else:
                
                count += f((n - m - 1), d)
        
        d[n] = count
        return count

N = int(input("> "))
d = {}

print(f(N, d))
    
    
