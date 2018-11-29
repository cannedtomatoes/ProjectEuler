#euler 99


import math


lines = []
f = open("p099_base_exp.txt")

for l in f.readlines():
	lines.append(l.replace("\n", ""))
	
f.close()
high_base = 1
high_exp = 1	


for i, line in enumerate(lines):
	
	entry = line.split(",")
	base = int(entry[0])
	exp = int(entry[1])
	
	LHS = math.log(high_base)/math.log(base)
	RHS = exp/high_exp
	
	if LHS < RHS:
		high_line = i
		high_base = base
		high_exp = exp
	
high_line += 1		
print(high_line)
