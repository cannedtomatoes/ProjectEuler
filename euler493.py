#euler 493

import math
import itertools

def how_many_of_each(distinct, total=20, upper=10):
    output = []

    remaining = total - distinct

    max_excess = upper - 1

    for combo in itertools.product(range(max_excess + 1), repeat=distinct):
        if sum(combo) == remaining:
            output.append(tuple(c + 1 for c in combo))

    return output
                
    


e = 0
total = math.comb(70, 20)

p_total = 0

for d in range(2, 8):
    favourable = 0
    for way in how_many_of_each(d):
        ways_for_this = 1
        for val in way:
            ways_for_this *= math.comb(10, val)
        favourable += ways_for_this
    favourable *= math.comb(7, d)
    
    p = favourable/total

    p_total += p
    print(d, p)

    e += (p * d)

print("Check p =", p_total)
print(e)
