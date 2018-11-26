#euler 92

from tqdm import tqdm

def next_link(n):
	n_digs = list(str(n))
	total = 0
	
	for digit in n_digs:
		dig_int = int(digit)
		total += dig_int**2
	
	return total

count = 0
	
for i in tqdm(range(1, 10000000)):
	
	while i != 89 and i != 1:
	
		i = next_link(i)
		
	if i == 89:
		count += 1
		
print(count)