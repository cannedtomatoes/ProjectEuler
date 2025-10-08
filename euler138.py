#euler 138

import math
from sympy.solvers.diophantine import diop_solve
from sympy import symbols
from sympy.abc import b, L


def one_even(n, m):
    return (n % 2) != (m % 2)

def gen_triples(maximum=1000):
    for n in range(1, maximum):
        for m in range(n + 1, maximum):  # m > n
            if math.gcd(n, m) == 1 and one_even(n, m):
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                yield a, b, c

m, L, t = symbols('m L t', integer=True)

eq1 = (m ** 2) - (5 * (L**2)) + 1

eq_sol = diop_solve(eq1)

(m_expr, L_expr) = next(iter(eq_sol))  # get first solution tuple

# Initial solution
m, L = 2, 1

result = 0

print("Integer solutions (m, L):")
for _ in range(1, 13):
    print(m, L)
    m, L = 9*m + 20*L, 4*m + 9*L
    
    if L == 1:
        continue
    else:
        result += L
        
print(result)
