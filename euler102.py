#euler 102

from sympy import *
from tqdm import tqdm
import math

f = open("p102_triangles.txt")

all_text = f.readlines()
f.close()

points = []

for a in all_text:
	points.append(a.replace('\n','').split(","))

solution = 0
	
for entry in points:
	
	A = (int(entry[0]), int(entry[1]))
	B = (int(entry[2]), int(entry[3]))
	C = (int(entry[4]), int(entry[5]))
	
	AB_dist = math.sqrt(math.pow((B[0] - A[0]), 2) + math.pow((B[1] - A[1]), 2))
	AC_dist = math.sqrt(math.pow((C[0] - A[0]), 2) + math.pow((C[1] - A[1]), 2))
	CB_dist = math.sqrt(math.pow((B[0] - C[0]), 2) + math.pow((B[1] - C[1]), 2))
	
	OA_dist = math.sqrt(math.pow(A[0], 2) + math.pow(A[1], 2))
	OB_dist = math.sqrt(math.pow(B[0], 2) + math.pow(B[1], 2))
	OC_dist = math.sqrt(math.pow(C[0], 2) + math.pow(C[1], 2))
	
	x = symbols('x')
	
	#Create equation for line AB
	
	#AB_exp = A[1] + ((B[1]-A[1])/(B[0]-A[0]))*(x-A[0])
		
	#AC_exp = A[1] + ((C[1]-A[1])/(C[0]-A[0]))*(x-A[0])

	#CB_exp = C[1] + ((B[1]-C[1])/(B[0]-C[0]))*(x-C[0])
	
	angle_AB = math.acos((math.pow(OA_dist, 2) + math.pow(OB_dist, 2) - math.pow(AB_dist, 2))/(2 * OA_dist * OB_dist))
	angle_AC = math.acos((math.pow(OA_dist, 2) + math.pow(OC_dist, 2) - math.pow(AC_dist, 2))/(2 * OA_dist * OC_dist))
	angle_CB = math.acos((math.pow(OC_dist, 2) + math.pow(OB_dist, 2) - math.pow(CB_dist, 2))/(2 * OB_dist * OC_dist))
	
	total = angle_AB + angle_AC + angle_CB
	total = round(total, 5)
	#print(total)
	if total == 6.28319:
		solution += 1
	
	
	
	
	
print("\nSolution: " + str(solution))