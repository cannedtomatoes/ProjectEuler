#euler 61

import itertools
from collections import defaultdict

def is_cyclic(nums):
    
    one = str(nums[0])
    two = str(nums[1])
    three = str(nums[2])
    
    # 0123 0123 0123
    # abcd cdef efab
    
    if one[2] != two[0]:
        return False
    elif one[3] != two[1]:
        return False
    elif two[2] != three[0]:
        return False
    elif two[3] != three[1]:
        return False
    elif three[2] != one[0]:
        return False
    elif three[3] != one[1]:
        return False
    else:
        return True
    
def triangle():
    # 45 to 140
    output = []
    n = 45
    t = (n * (n + 1))/2
    output.append(int(t))
    
    while n <= 140:
        t = (n * (n + 1))/2
        #print("n = " + str(n) + ", t = " + str(t))
        output.append(int(t))
        n += 1

    return output

def square():
    #32 to 99
    output = []
    n = 32
    s = n*n
    output.append(int(s))
    
    while n <= 99:
        s = n*n
        output.append(int(s))
        n += 1
        
    return output

def pentagon():
    # 26 to 81
    output = []
    n = 26
    p = (n * ((3 * n) - 1))/2
    output.append(int(p))
    
    while n <= 81:
        p = (n * ((3 * n) - 1))/2
        #print("n = " + str(n) + ", t = " + str(p))
        output.append(int(p))
        n += 1

    return output

def hexagon():
    # 23 to 70
    output = []
    n = 23
    h = n * ((2 * n) - 1)
    output.append(int(h))
    
    while n <= 70:
        h = n * ((2 * n) - 1)
        #print("n = " + str(n) + ", t = " + str(p))
        output.append(int(h))
        n += 1

    return output

def heptagon():
    # 21 to 63
    output = []
    n = 21
    hp = (n * ((5 * n) - 3))/2
    output.append(int(hp))
    
    while n <= 63:
        hp = (n * ((5 * n) - 3))/2
        #print("n = " + str(n) + ", t = " + str(p))
        output.append(int(hp))
        n += 1

    return output

def octagon():
    # 19 to 58
    output = []
    n = 19
    o = n * ((3 * n) - 2)
    output.append(int(o))
    
    while n <= 58:
        o = n * ((3 * n) - 2)
        #print("n = " + str(n) + ", t = " + str(p))
        output.append(int(o))
        n += 1

    return output

def first_two(num):
	return str(num)[:2]
	
def last_two(num):
	return str(num)[2:]

def scrub(poss, keep):

    new = []

    for po in poss:

        if len(po) == keep:
            new.append(po)

    return new


def insert(poss, num_set, initial, final):

    for n in num_set:

        for p in poss:

            if initial:
                first = p[0]
                last = p[0]

                if last_two(last) == first_two(n):
                    p.append(n)

                elif last_two(n) == first_two(first):
                    p.insert(0, n)

            elif final:

                first = p[0]
                last = p[len(p)-1]
                
                if last_two(last) == first_two(n) and last_two(n) == first_two(first):
                    p.append(n)


                elif last_two(n) == first_two(first) and first_two(n) == last_two(last):
                    p.insert(0, n)

            else:

                first = p[0]
                last = p[len(p)-1]
                
                if last_two(last) == first_two(n):
                    p.append(n)

                elif last_two(n) == first_two(first):
                    p.insert(0, n)


def initi(poss, num_set):

    for n in num_set:
        poss.append([n])

    
triangles = triangle()
squares = square()
pentagons = pentagon()
hexagons = hexagon()
heptagons = heptagon()
octagons = octagon()

pos = []

#tri, sq, pent, hex, hep, oct X
#tri, sq, pent, hep, hex, oct 

vals = list(itertools.permutations([1, 2, 3, 4, 5, 6]))

for v in vals:

    if v[0] == 1:
        s1 = triangles
    elif v[0] == 2:
        s1 = squares
    elif v[0] == 3:
        s1 = pentagons
    elif v[0] == 4:
        s1 = hexagons
    elif v[0] == 5:
        s1 = heptagons
    elif v[0] == 6:
        s1 = octagons

    if v[1] == 1:
        s2 = triangles
    elif v[1] == 2:
        s2 = squares
    elif v[1] == 3:
        s2 = pentagons
    elif v[1] == 4:
        s2 = hexagons
    elif v[1] == 5:
        s2 = heptagons
    elif v[1] == 6:
        s2 = octagons    

    if v[2] == 1:
        s3 = triangles
    elif v[2] == 2:
        s3 = squares
    elif v[2] == 3:
        s3 = pentagons
    elif v[2] == 4:
        s3 = hexagons
    elif v[2] == 5:
        s3 = heptagons
    elif v[2] == 6:
        s3 = octagons    

    if v[3] == 1:
        s4 = triangles
    elif v[3] == 2:
        s4 = squares
    elif v[3] == 3:
        s4 = pentagons
    elif v[3] == 4:
        s4 = hexagons
    elif v[3] == 5:
        s4 = heptagons
    elif v[3] == 6:
        s4 = octagons

    if v[4] == 1:
        s5 = triangles
    elif v[4] == 2:
        s5 = squares
    elif v[4] == 3:
        s5 = pentagons
    elif v[4] == 4:
        s5 = hexagons
    elif v[4] == 5:
        s5 = heptagons
    elif v[4] == 6:
        s5 = octagons

    if v[5] == 1:
        s6 = triangles
    elif v[5] == 2:
        s6 = squares
    elif v[5] == 3:
        s6 = pentagons
    elif v[5] == 4:
        s6 = hexagons
    elif v[5] == 5:
        s6 = heptagons
    elif v[5] == 6:
        s6 = octagons


    initi(pos, s1)

    #print(pos)

    insert(pos, s2, True, False)

    pos = scrub(pos, 2)
    #print(pos)                    	

    insert(pos, s3, False, False)

    pos = scrub(pos, 3)
    #print(pos)
                    	
    insert(pos, s4, False, False)

    pos = scrub(pos, 4)
    #print(pos)
                    	
    insert(pos, s5, False, False)

    pos = scrub(pos, 5)
    #print(pos)
                    	
    insert(pos, s6, False, True)

    pos = scrub(pos, 6)

    if pos:

        print(pos)
        
        print("Sum = " + str(sum(pos[0])))
