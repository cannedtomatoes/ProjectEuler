#euler 85

import itertools
from tqdm import tqdm

def recs(m, n):
	return int((m*(m+1)*n*(n+1))/4)

	
min_diff = 2000000

options = range(1, 1001)

for x in itertools.combinations(options, 2):
	
	diff = abs(2000000 - recs(x[0], x[1]))
	
	
	if diff < min_diff:
		min_diff = diff
		wm = x[0]
		wn = x[1]

		
print("m = " + str(wm) + ", n = " + str(wn))
print("Area = " + str(wm*wn))
		