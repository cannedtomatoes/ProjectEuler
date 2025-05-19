from sympy.utilities.iterables import multiset_permutations
import math
import itertools

def solve(size, tar):

    result = 0

    num = [1,2,3,4]

    for comb in itertools.combinations_with_replacement(num, size):

        #print(lst)
        
        if sum(comb) == tar:

            #print(comb)

            denominator = 1
                    
            for d in set(comb):

                denominator *= math.factorial(comb.count(d))
            
            #print("Size =", size, "size-i=", size-i)
            to_add = math.factorial(size)/denominator

            result += to_add

            #print("Added", to_add)
            
            #result += len(list(multiset_permutations(lst)))
            #print(list(multiset_permutations(lst)))
        
    return result

target = 50
done = 0

for m in range(1, target+1):

    print("m =", m)
    done += solve(m, target)

print(done)
