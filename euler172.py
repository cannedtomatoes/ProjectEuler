#euler 172
# How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?
#227485267000992000

import math
import itertools

def valid(olist):

    seen = []

    for o in olist:

        if o[0] not in seen:
            seen.append(o[0])
        else:
            return False

    return True

def arrangements(obj_list):

    den = 1

    for ob in obj_list:

        den = den * math.factorial(ob[1])

    den2 = 1

    if obj_list[0][0] == 0:

        for ob in obj_list:

            if ob[0] == 0:

                den2 = den2 * math.factorial(ob[1]-1)

            else:

                den2 = den2 * math.factorial(ob[1])

        return (6402373705728000/den) - (355687428096000/den2)

            

    else:

        return (6402373705728000/den)

#Most numbers used - 8 digits occur twice, 2 occur once
#112233445566778890

#Fewest numbers used - 6 digits occur thrice
#111222333444555666

e = []

for i in range(0, 10):

    for j in range(1, 4):

        e.append((i, j))

solns = []

result = 0

print("Generating combinations...")

for k in range(6, 11):

    print("k =", k)

    for comb in itertools.combinations(e, k):

        if valid(comb):

            total_digs = 0
            
            for c in comb:

                total_digs += c[1]

            if total_digs == 18:

                solns.append(comb)
                #print(comb)

print("Done")
print("Calculating arrangements...")

for s in solns:

    result += arrangements(s)

print("Done")

print(result)
print("{:.90f}".format(result))


    
