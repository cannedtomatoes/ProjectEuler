#euler 144

from sympy import * 
import math

def convert(radians):
	return radians * (180/math.pi)


def grad_l(xa, ya, xb, yb):
	return (yb-ya)/(xb-xa)

def check(x_c, y_c):
	
	return (y_c > 0 and x_c > -0.01 and x_c < 0.01)
		


x,y=symbols('x y') 
count = 0
wc = Eq((4*(x*x))+(y*y), 100)

#res = wc.subs(x,0)
x1 = 0
y1 = 10.1

x2 = 1.4
y2 = -9.6

while True:
	
	m_t = (-4 * x2)/y2
	m_n = -1 * m_t
	m_p = grad_l(x1, y1, x2, y2)
	
	#angle_i = angle(m_p)
	
	angle_g = math.atan(m_t)
	
	if angle_g < 0:
		angle_g = math.pi-abs(angle_g)
	
	angle_i = math.atan(m_p)
	
	if angle_i < 0:
		angle_i = math.pi-abs(angle_i)
	
	angle_r = angle_i + (math.pi - (2*(angle_i - angle_g)))
	
	if angle_r < 0:
		angle_r = math.pi-abs(angle_r)
	
	
	#print("Angle_i = " + str(convert(angle_i)))
	#print("Theta = " + str(convert(angle_g)))
	#print("Angle_r = " + str(convert(angle_r)))
	#print("x1 = " + str(x1))
	#print("y1 = " + str(y1))
	#print("x2 = " + str(x2))
	#print("y2 = " + str(y2))
	
	
	m_r = math.tan(angle_r)
	
	sline = Eq(y, ((m_r*x)-(m_r*x2)+y2))
	
	
	#print(sline)
	
	res = solve([wc, sline], (x,y))
	#print(res)

	for point in res:
	

		#Find which is the new x val
	
		if not math.isclose(point[0], x2, abs_tol=0.00001):
			new_point = point

			#print(str(point[0]) + "     !=      " + str(x2))
			print(new_point)
			#input()
			
	x1 = x2
	y1 = y2
	
	x2 = new_point[0]
	y2 = new_point[1]
	
	count += 1
	
	if check(x2, y2):
		print("Winner!")
		print(count)
		exit()

	
