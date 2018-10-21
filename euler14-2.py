#euler14
#Which starting number, under one million, produces the longest chain?
#Second revision 

#n -> n/2 (n even)
#n -> 3n + 1 (n odd)

from tqdm import tqdm

def collatz(n):
	#returns number in the chain
	l = 1
	#print("New number: " + str(n))
	while n != 1:
		
		try:
			l += history[n]
		except:
			if n % 2 == 0:
				n = n / 2
			else:
				n = (3*n) + 1
			l += 1
		else:
			n = 1
			
		
		
		#print("n = " + str(n))
		
	return l
	
longest = 0
result = 0
	
history = {}	
	
for t in tqdm(range(1, 1000000)):
	
	new = collatz(t)
	
	history[t] = new
	#print(str(t) + " (" + str(new) + ")")
	if new > longest:
		#print("New longest, t = " + str(t) + " (" + str(new) + ")")
		longest = new
		result = t
		

		
print(result)
print(longest)