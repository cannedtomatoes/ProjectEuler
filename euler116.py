from sympy.utilities.iterables import multiset_permutations
import math


def solve(num, size, tar):

    result = 0

    for i in range(1, size+1):

        lst = []

        #print("List will have " + str(i) + " " + str(num) + "'s and " + str(size-i) + " 1's")
        
        for k in range(i):
            lst.append(num)
        
        for j in range(size-i):
            lst.append(1)

        
        
        if sum(lst) > tar:
            return result

        #print(lst)
        
        
        if sum(lst) == tar:
            #print("Size =", size, "size-i=", size-i)
            to_add = math.factorial(size)/(math.factorial(i) * math.factorial(size-i))    

            result += to_add

            #print("Added", to_add, "size =", size)
            
            #result += len(list(multiset_permutations(lst)))
            #print(list(multiset_permutations(lst)))
        
    return result

target = 50
done = 0

for n in range(2, 5):

    print("n =", n)

    for m in range(1, target):

        print("m =", m)
        done += solve(n, m, target)

print(done)
