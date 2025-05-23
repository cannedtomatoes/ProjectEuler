#euler 139
import math
import sys

def gen_prims(N):

    for m in range(1, N):
	    for n in range(1, N):
			
	        #sys.stdout.write("\r" + str(count) + " primitives checked")
		    #sys.stdout.flush()
		    if m > n:
			    both_odd = (m % 2 != 0) and (n % 2 != 0)
			    if not both_odd:
				    if math.gcd(m,n) == 1:
				    
				    	#primitive
				    	a = m**2 - n**2
				    	b = 2*m*n
				    	c = m**2 + n**2
						
				    	yield a, b, c

target = 100000000
count = 0

for a, b, c in gen_prims(1000000):
    
    p = [a, b, c]
    
    prim_sum = sum(p)
    
    sys.stdout.write("\r" + str(count) + " (" + str(prim_sum) + ")")
    sys.stdout.flush()
    

        
    k = 1
    a1 = a * k
    b1 = b * k
    c1 = c * k

    p = [a1, b1, c1]
    sump = sum(p)

    while sump < target:
        
        square_area = c1*c1
            
        triangles_area = 4 * 0.5 * a1 * b1
            
        hole = square_area-triangles_area
            
        if square_area % hole == 0:
            
            count += 1
                
            
        k+= 1
        a1 = a * k
        b1 = b * k
        c1 = c * k

        p = [a1, b1, c1]
        sump = sum(p)
	
							
	
