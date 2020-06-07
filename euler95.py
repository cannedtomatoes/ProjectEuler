#euler 95

import math
import sys
from tqdm import tqdm
import ast
import random

def miller(n):

    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True 

def divisor_gen(n):

	end = int(math.ceil(math.sqrt(n)))

	for i in range(1, end):
		if n % i == 0:
			yield i
			print(i)

def factors(n):
  if n == 0: return []
  factors = {1, n}
  for i in range(2, math.floor(n ** (1/2)) + 1):
	  if n % i == 0:
            factors.add(i)
            factors.add(n // i)
  return list(factors)
  
def div_sum(n):
	
	total = 0
	
	for d in factors(n):
		
		total += d
		
	return (total - n)
	

d = {}



for i in tqdm(range(1, 1000001)):
        
    ds = div_sum(i)
    
    if ds <= 1000000:
        d[i] = ds
    else:
        d[i] = -1
    

longest = 0
output = 0
first = 0

for i in tqdm(range(1, 1000001)):
#for i in range(1, 1000001):

    

    #print("New")
    
    
    
    if miller(i):
        continue
    
    chain = [i]
    failed = False
    done = False
    amic = False
    current = i
    
    
    while not failed and not done:
        
        #print(i)
        #print(chain)
        #input()
        
        try:
            next_item = d[current]
        except:
            failed = True
        
        if next_item == -1:
            failed = True
            
        else:
            if next_item not in chain:
                chain.append(next_item)
                current = next_item
                if miller(next_item):
                    done = True
                    #print("prime: " + str(next_item))
            else:
                done = True
                if next_item == i:
                    chain.append(next_item)
                    amic = True
                
    if done and amic:
        
        length = len(chain)
        #print(chain)
        #input()
        
        #print(str(i) + " has " + str(length) + " in the chain")
        
        if length > longest:
            longest = length
            smallest = min(chain)
            first = i
            
            

print("Longest length: " + str(longest))
print("First element: " + str(first))
print("Smallest element: " + str(smallest))

    #print(i)
    
    #sys.stdout.write("\r" + str(i) + ": " + str(cl))
    #sys.stdout.flush()