#euler 100

#Given y being total discs and x being blue discs we have equation
#2x^2 - 2x - y^2 + y = 0
#Find the first solution to this equation with y > 10^2
#This website given recursive solutions to the equation
#https://www.alpertron.com.ar/QUAD.HTM
#x_n+1 = 3x_n + 2y_n - 2
#y_n+1 = 4x_n + 3y_n -3
#
#with x1 = 1, y1 = 1

import math
import sys

y1 = 1
x1 = 1

while True:
	
	x = (3*x1) + (2*y1) - 2
	y = (4*x1) + (3*y1) - 3
	
	if y > 10**12:
		print(x)
		print(y)
		break
	else:
		y1 = y
		x1 = x