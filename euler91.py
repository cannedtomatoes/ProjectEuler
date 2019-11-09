#Euler 91
#14234

import itertools
from tqdm import tqdm
import math

def grad(p1, p2):
	return (p2[1] - p1[1]) / (p2[0] - p1[0])

def dist(p1, p2):

	return math.sqrt(math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2))

def cos_rule_angle(x, y, z):
	
	return math.acos((math.pow(x,2) + math.pow(y,2) - math.pow(z,2)) / (2 * x * y))
	
points = []

for i in range(51):
	
	for j in range(51):
	
		points.append((i,j))
		
del points[0]

#print(points)
#print(len(points))

count = 0
origin = (0,0)

for comb in tqdm(itertools.combinations(points, 2)):
	
	#comb = ((0,2), (1,1))
	
	a = dist(origin, comb[0])
	b = dist(origin, comb[1])
	c = dist(comb[0],comb[1])
	
	try:
		angle1 = cos_rule_angle(a, b, c)
	except:
		continue
	try:
		angle2 = cos_rule_angle(c, a, b)
	except:
		continue
	try:
		angle3 = cos_rule_angle(b, c, a)
	except:
		continue
	
	#print(angle1)
	#print(angle2)
	#print(angle3)
	
	if round(angle1, 6) == round((math.pi/2), 6):
		count += 1
		#print(comb)
	elif round(angle2, 6) == round((math.pi/2), 6):
		count += 1
		#print(comb)
	elif round(angle3, 6) == round((math.pi/2), 6):
		count += 1
		#print(comb)
	

	
print(count)