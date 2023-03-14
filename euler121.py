#euler121

import itertools
from collections import Counter
from fractions import Fraction

prob = 0

pair = ['R', 'B']

rounds = 15


seen = []
c = Counter()
d = Counter()

p_total = Fraction(0)

all_branches = []


for comb in itertools.product(pair, repeat=rounds):

    p = Fraction(1)


    #print(comb)
    #input()
    
    c[comb] += 1
    if c[comb] != 1:
        continue

    if comb.count('B') > comb.count('R'):



        #print(comb)
        
        j = 0

        while j < len(comb):

            if comb[j] == 'R':

                p = p * Fraction(j+1, j+2)
                #print("Multiplying by " + str(j+1) + "/" + str(j+2))

            elif comb[j] == 'B':

                p = p * Fraction(1, j+2)
                #print("Multiplying by " + "1/" + str(j+2))


            j += 1
            #input()

        p_total += p

print(p_total)
                





