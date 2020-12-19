#euler 587

import numpy
import math
from scipy.integrate import quad


    
def g(x):
    return 1-math.sqrt((2*x)-(x*x))

#orig = (1-(numpy.pi * 0.25))/4

orig, err0 = quad(g, 0, 1)

circles = 1

while True:

    #point of intersection
    grad = 1/circles
    a = (grad*grad)+1
    b = -2 + (-2*grad)
    c = 1

    pos_mid = numpy.roots([a, b, c])

    mid = min(pos_mid)
    #print(mid)

    a1 = 0.5 * mid * (1/circles) * mid



    #a1 triangle, a2 curved

    #a1, err1 = quad(f, 0, mid)
    a2, err2 = quad(g, mid, 1)

    total = a1 + a2

    #print(a1)
    #print(a2)
    #print(total)
    #print(orig)

    ratio = total/orig
    print("c = " + str(circles) + ", r = " + str(ratio))
    
    if ratio < 0.001:
        break
    
    circles += 1