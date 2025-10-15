#euler 188

from sympy.functions.combinatorial.numbers import totient
import math

m = 10**8

M = []

T = []

a = 1777
b = 1855

i = 0

print("Going down the tower")

while i < b - 1:

    #print("m_" + str(i) + " = " + str(m))
    
    t = totient(m)
    T.append(t)
    M.append(m)
    
    m = t

    i += 1

print()

r = pow(a, a, int(t))
i -= 1

print("Headed back up")

while i >= 0:

    R = pow(a, r, int(M[i]))
    
    #print("R_" + str(i) + " = " + str(R))

    r = R
    
    i -= 1

print(R)


