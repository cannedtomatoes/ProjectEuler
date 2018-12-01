#euler 104

import sys

def fib():
	a, b = 0, 1
	while True:            # First iteration:
		yield a            # yield 0 to start with and then
		a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
		
def pandigital(big_list):
	
	all_numbers = sorted(big_list)
	

	all_numbers_str = ''.join(all_numbers)
	#print(all_numbers_str)

	if all_numbers_str == '123456789':
		return True
	else:
		return False

count = 0		
for f in fib():
	
	
	sys.stdout.write("\rChecking F_" + str(count))
	sys.stdout.flush()
	
	digs = str(f)
	if len(digs) >= 18:
		start = digs[:9]
		end = digs[-9:]
		
		if pandigital(start) and pandigital(end):
			print("\nFinal: " + str(count))
			print("Length: " + str(len(digs)))
			exit()
			
	count += 1