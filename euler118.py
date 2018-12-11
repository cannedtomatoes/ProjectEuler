# euler 118

import random
import itertools
from tqdm import tqdm
import sys
from collections import Counter
import time

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

def pandigital(big_list):
	
	all_numbers = sorted(big_list)
	

	all_numbers_str = ''.join(all_numbers)
	#print(all_numbers_str)

	if all_numbers_str == '123456789':
		return True
	else:
		return False

def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def num_digits(n):
	answer = 1
	f = 10
	
	while f < n:
		f *= 10
		answer += 1
	
	return answer

def make_number(digits):
	#takes list of chars and turns them into an int
	return int(''.join(digits))

all_sets = []
parts = []
for p in partitions(9):
	parts.append(p)
	
# Create all pandigital sets of numbers
# Check if each prime

count = 0
all_sets = []
max_len = 0

for perm in tqdm(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'])):

	#Split each into different sets numbers based on partitions
	

	for part in parts:
		
		worked = True
		new_set = []
		start = 0
		#print(part)
		
		for p in part:
			
			if p:
				
				length = p
				end = start + length
				this_num_list = perm[start:end]
				#print("[" + str(start) + ":" + str(p) + "]")
				#print("Sending " + str(this_num_list) + " to make_number")
				number = make_number(this_num_list)
				new_set.append(number)
				start = end
			
				#print("Made number " + str(number))
				#input()
		
		for n in new_set:
			if not miller(n):
				worked = False
				break
			
		if worked:
			all_sets.append(sorted(new_set))
			#print(new_set)
			#count += 1
			#if len(new_set) > max_len:
				#max_len = len(new_set)
				#print(new_set)

unique_sets = []
	
for s in tqdm(all_sets):
	if s not in unique_sets:
		unique_sets.append(s)


print(len(unique_sets))		
	
	
	

