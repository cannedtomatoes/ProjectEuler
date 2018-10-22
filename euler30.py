#euler30

from tqdm import tqdm

results = []


for i in tqdm(range(2, 1000000)):
	lst = list(str(i))
	s = 0
	
	#print(i)
	
	for n in lst:
		s += (int(n)**5)
		#print(str(n) + "^5")
		#print("+")
		
	#print(" = " + str(s))	
	if s == i:
		results.append(i)
		
print(results)
print(str(sum(results)))