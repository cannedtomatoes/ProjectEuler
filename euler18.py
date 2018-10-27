#euler 18

def available(index):
	if index == 0:
		return [0]
	else:
		return [index-1, index]
	
lines = []
lines.append(75)
lines.append([95, 64])
lines.append([17, 47, 82])
lines.append([18, 35, 87, 10])
lines.append([20, 4, 82, 47, 65])
lines.append([19, 1, 23, 75, 3, 34])
lines.append([88, 2, 77, 73, 7, 63, 67])
lines.append([99, 65, 4, 28, 6, 16, 70, 92])
lines.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
lines.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
lines.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
lines.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
lines.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
lines.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
lines.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

base_line = lines[14]
i = 13
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
	
print(str(max(base_line[0], base_line[1]) + lines[0]))