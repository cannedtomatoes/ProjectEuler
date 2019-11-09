#euler 179

from tqdm import tqdm
import math



facts = {}
done = False

fact = 2
	
for fact in tqdm(range(2, 10000000)):
		
	mult = 0

	while mult < 10000000:

		mult += fact
		
		if mult in facts:
			facts[mult].append(fact)
			#print("Added " + str(fact) + " as factor of " + str(mult))
		else:
			facts[mult] = [fact]
			#print("Added " + str(fact) + " as factor of " + str(mult))

	#fact += 1
	#print(fact)
	
print("\nFinding solutions\n")

test = 2
output = 0

for test in tqdm(range(2, 9999999)):
	
	if facts[test] == facts[test + 1]:
		output += 1
	
	
print(output)