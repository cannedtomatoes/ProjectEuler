#euler 15

#Goes down when i = 20
#Last one to go down i = 0

grid = []

for i in range(0, 21):
	grid.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
	
for c in grid:
	print(''.join(c))
	
grid_orig = grid

#Go to the right until you hit element id
#Start going down until you hit the bottom
#Go to the right until you hit the final square

row_index = 0
down_index = 20
finished = False

while not finished:
	current_row = grid[row_index]
	
	for i in range(0, down_index):
		
	
	