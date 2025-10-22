#euler 191

import math

# O - on time
# L - late
# A - absent

N = 30

total_valid_arrangements = 0

for L in range(0, 2):
    
    remaining = N - L
    
    for A in range(0, remaining + 1):
        
        O = remaining - A

        total_arrangements = math.factorial(N)/(math.factorial(L)*math.factorial(O)*math.factorial(A))

        non_A_arrangements = math.factorial(L+O)/(math.factorial(L)*math.factorial(O))

        S = math.comb(A + (L + O), L + O)

        A_arrs = 0

        for j in range(0, math.floor(A/3)+1):

            A_arrs += (-1)**j * math.comb(L + O + 1, j) * math.comb(N - (3*j), L + O)


        valid_A_varrs = non_A_arrangements * A_arrs


        print(L, "L(s)", A, "A(s)", O, "O(s)", valid_A_varrs, " arrangements")
        #input()
        
        total_valid_arrangements += valid_A_varrs
        
        
print(total_valid_arrangements)
