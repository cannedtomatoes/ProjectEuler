#euler 94

#from sympy import factorint
from sympy.solvers.diophantine.diophantine import diop_DN
from math import sqrt, ceil

#print(diop_DN(3,1))

#m = 2, n = 1 is fundamental solution of m^2 - Dn^2 = 1

#Use recurrence relation to find the rest

#x_k+1 = x_0 x_k + D y_0 y_k
#y_k+1 = x_0 y_k + y_0 x_k


D = 3
m0 = 2
n0 = 1

mk = m0
nk = n0

total = 0

#Triangle sides
a = (m0**2) - (n0**2)
b = 2*m0*n0
c = (m0**2) + (n0**2)

#Triangle perimeter
p = (2*c) + (2*a)



results = []
results.append(p)
print("a b c m n p A")

print(a, b, c, m0, n0, p)

while True:

        m = (m0 * mk) + (D * n0 * nk)
        n = (m0 * nk) + (n0 * mk)


        #Triangle sides
        a = (m**2) - (n**2)
        b = 2*m*n
        c = (m**2) + (n**2)

        #Triangle perimeter
        p = (2*c) + (2*a)

        if p > 1000000000:
                break
        else:
                results.append(p)

        
        print(a, b, c, m, n, p)
        #input()
        
        mk = m
        nk = n

#Second equation for where 2b - c = -1 solved using sympy 
t = 0
while True:
        
        m = ceil(-7*sqrt(3)*(2 - sqrt(3))**t/6 + 2*(2 - sqrt(3))**t + 2*(sqrt(3) + 2)**t + 7*sqrt(3)*(sqrt(3) + 2)**t/6)
        n = ceil(-sqrt(3)*(2 - sqrt(3))**t/3 + (2 - sqrt(3))**t/2 + (sqrt(3) + 2)**t/2 + sqrt(3)*(sqrt(3) + 2)**t/3)

        #Triangle sides
        a = (m**2) - (n**2)
        b = 2*m*n
        c = (m**2) + (n**2)

        #Triangle perimeter
        p = (2*c) + (2*b)

        if p > 1000000000:
                break
        else:
                results.append(p)

        
        print(a, b, c, m, n, p)

        t += 1




print("Total: " + str(sum(results)))
        
