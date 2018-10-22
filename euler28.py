#euler 28


	
grid = {}
	
#Grid dimension increase by 2 each iteration, ie 1^2, 3^2, 5^2, 7^2 etc...
	
size = 1
i = 1
# Centre number is the origin
x = 0
y = 0

grid[(x,y)] = i
i += 1
#print(str(x) + ", " + str(y))
while size < 1001:
	
	#Move point one unit to the right
	x +=1
	grid[(x,y)] = i
	i +=1 
	#print(str(x) + ", " + str(y))	
	#Move point size units down, creating a point each time
	
	temp_y = y
	while y > (temp_y - size):
		#print("Loop 1: while " + str(y) + " >= " + str(y - size))
		y -= 1
		grid[(x,y)] = i
		#print(str(x) + ", " + str(y))

		i += 1
		

	#Move point size+1 units left, creating a point each time
	temp_x = x
	while x > (temp_x - (size + 1)):
		x -= 1
		grid[(x,y)] = i
		i += 1
		#print(str(x) + ", " + str(y))


	#Move a point size+1 units up, creating a point each time
	temp_y = y
	while y < (temp_y + size + 1):
		y += 1
		grid[(x,y)] = i
		i += 1	
		#print(str(x) + ", " + str(y))

	#Move point size+1 units right, creating a point each time
	temp_x = x
	while x < (temp_x + size + 1):
		x += 1
		grid[(x,y)] = i
		i += 1	
		#print(str(x) + ", " + str(y))

		
	size += 2

#Add diagonals
#
#(-2,2) (-1,2)  (0,2)  (1,2)  (2,2)
#(-2,1) (-1,1)  (0,1)  (1,1)  (2,1)
#(-2,0) (-1,0)  (0,0)  (0,1)  (2,0)
#(-2,-1)(-1,-1) (0,-1) (1,-1) (2,-1)
#(-2,-2)(-1,-2) (0,-2) (1,-2) (2,-2)

d = int((size - 1)/2)

sum = 0

for k in range((-1*d), (d+1)):
	x_c = k
	y_c = -1*k
	sum += grid[(x_c, y_c)]
	sum += grid[(k,k)]
	
sum -= 1

print(sum)		
		
		
