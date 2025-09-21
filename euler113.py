#euler113

import math

def inc(digs):

    a = 9 + digs - 1


    return math.comb(a, digs)

def dec(digs):

    b = 10 + digs - 1

    return math.comb(b, digs) - 1

def nonb(digs):

    return inc(digs) + dec(digs) - 9

total = 0

for i in range(1, 101):

    total += nonb(i)

    print(total)
