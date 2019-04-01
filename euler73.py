#euler 73

from tqdm import tqdm
from math import gcd
import random
from queue import Queue
from fractions import Fraction

def farey(n, descending=False):
    """Print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    if descending: 
        a, c = 1, n-1
    yield (a,b)
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        yield(a,b)


highest = 12000
result = 0



for f in tqdm(farey(highest)):
	
	q = f[0]/f[1]
	
	if q > (1/3) and q < (1/2):
		result += 1
		
print(result)


			
				