#euler 140

#Generating function for S(x) = sum of (A_n x^n) given A_1 = 1 A_2 = 4
#S = (x + 3x^2)/(1-x-x^2)

# D = 5S + 14S + 1

from sympy import symbols
from sympy.solvers.diophantine import diophantine
import math

def is_square(n):
    r = math.isqrt(n)
    return r * r == n



S, x, y = symbols('S, x, y')
#eqn = (5*(S**2)) - (y**2) + (14*S) + 1
eqn = (x**2) - (5*(y**2)) - 44
solutions = diophantine(eqn)
#print(solutions)
#input()

results = []

for sol in solutions:

    x_expr, y_expr = sol
    # Find the parameter in the first expression
    param = list(x_expr.free_symbols - {x, y})[0]
    
    for t_val in range(-1000, 1001):
    
        x_sol = x_expr.subs(param, 0)
        y_sol = y_expr.subs(param, 0)
    
        if x_sol.is_integer:
        
            x1 = x_sol
            y1 = y_sol
            
            if (x_sol, y_sol) not in results:
                results.append((x_sol, y_sol))


#print(results)
#input()

#seeds = [(7,1), (8,2), (13,5), (17,7)]
#results = [2, 5, 21, 42, 152, 296, 1050, 2037, 7205, 13970, 49392, 95760, 338546, 656357, 2320437, 4498746, 15904520, 30834872, 109011210, 211345365, 747173957, 1448582690] #found in previous version, just need 2 more!!

seeds = [(7,1), (8,2), (13,5), (17,7)]
results = set()

# Forward and backward Pell iteration
for x0, y0 in seeds:
    for direction in ["forward", "backward"]:
        x, y = x0, y0
        count = 0
        while count < 50:  # enough iterations to capture all small S
            # Check S
            if (x - 7) % 5 == 0:
                S = (x - 7) // 5
                if S > 0:
                    results.add(S)
                    count += 1
            # Apply Pell recurrence
            if direction == "forward":
                x, y = 9*x + 20*y, 4*x + 9*y
            else:
                x, y = 9*x - 20*y, -4*x + 9*y

# Collect and sort the first 30 golden nuggets
golden_nuggets = sorted(results)[:30]
print("First 30 golden nuggets:", golden_nuggets)
print("Sum of first 30:", sum(golden_nuggets))


