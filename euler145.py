#Euler 145

import math

from tqdm import tqdm

def num_digs(n):
	output = 0
	while n > 1:
		output += 1
		n = n / 10
		
	return output		
	

def leadz(n):
	digs = list(str(n))
	return digs[0] == '0'
	
def trailz(n):
	digs = list(str(n))
	return digs[len(digs)-1] == '0'	
	
	
def rev(n):
	n_str = str(n)
	return int(n_str[::-1])	
	
def all_odd(n):

	d_odd = {'0': 0, '1': 1, '2': 0, '3': 1, '4': 0, '5': 1, '6': 0, '7': 1, '8': 0, '9': 1}
	
	digs = list(str(n))
	
	for d in digs:
		if d_odd[d] == 0:
			return False
	
	return True


	
result = 0
for i in tqdm(range(1, int(math.pow(10,9)))):
	
	if not trailz(i):
	
		i_r = rev(i)
	
	#if int(math.log10(i))+1 == int(math.log10(i_r))+1:
	#if num_digs(i) == num_digs(i_r):
		
		test = i + i_r
		
		if all_odd(test):
			result += 1
		
print(result)
