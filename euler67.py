#euler 18

def available(index):
	if index == 0:
		return [0]
	else:
		return [index-1, index]

f = open("p067_triangle.txt")
		
lines1 = f.readlines()
f.close()
lines = []
for line in lines1:
	this_line_strs = line.split()
	this_line_ints = []
	for n in this_line_strs:
		this_line_ints.append(int(n))
	lines.append(this_line_ints)

	
base_line = lines[99]
i = 98
total = 0

while i > 0:

	new_line = []
	
	line_above = lines[i]

	j = 0

	while j < len(base_line):
		try:
			#print("Two posibilities: " + str(base_line[j]) + " + " + str(line_above[j]) + " and " + str(base_line[j+1]) + " + " + str(line_above[j]))
			sub_max = max((base_line[j] + line_above[j]), (base_line[j+1] + line_above[j]))
		except:
			break
		else:
			new_line.append(sub_max)
			j += 1
	
	base_line = new_line
	#print(base_line)

	i-= 1
	
print(str(max(base_line[0], base_line[1]) + lines[0][0]))