#euler 504

import sys
import math

def is_square(n: float) -> bool:
    if not n.is_integer():
        return False
    root = math.isqrt(int(n))
    return root * root == int(n)

def g_area(xs, ys):

    return 0.5 * ( ((xs[0] * ys[1]) - (xs[1] * ys[0])) + ((xs[1] * ys[2]) - (xs[2] * ys[1])) + ((xs[2] * ys[3]) - (xs[3] * ys[2])) + ((xs[3] * ys[0]) - (xs[0] * ys[3])) )

def l_points(xs, ys):
    
    total = 0
    
    #01
    test1 = abs(xs[1] - xs[0])
    test2 = abs(ys[1] - ys[0])
    total += 1 + math.gcd(test1, test2)
    
    #12
    test1 = abs(xs[2] - xs[1])
    test2 = abs(ys[2] - ys[1])
    total += 1 + math.gcd(test1, test2)
    
    #23
    test1 = abs(xs[3] - xs[2])
    test2 = abs(ys[3] - ys[2])
    total += 1 + math.gcd(test1, test2)
    
    #30
    test1 = abs(xs[0] - xs[3])
    test2 = abs(ys[0] - ys[3])
    total += 1 + math.gcd(test1, test2)
    
    return total - 4

m = 100
count = 0

for a in range(1, m+1):

    sys.stdout.write('\r' + "a = " + str(a) + ", Count = " + str(count))
    sys.stdout.flush()

    for b in range(1, m+1):
    
        for c in range (1, m+1):
        
            for d in range(1, m+1):
            
                xs = [a, 0, (-1 * c), 0]
                ys = [0, b, 0, (-1 * d)]
                
                A = g_area(xs, ys)
                B = l_points(xs, ys)
                
                P = A - (B/2) + 1
                
                if is_square(P):
                    
                    #print("a =", a, "b =", b, "c =", c, "d =", d, "A =", A, "P =", P, "B =", B)
                    count += 1

                    
print()
print(count)

                    
        
                    
