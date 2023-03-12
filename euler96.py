#euler 96

total = 0

def print_puz(puz):

    for row in puz:

        line = []

        line.append(str(row[0]))
        line.append(str(row[1]))
        line.append(str(row[2]))
        line.append(" ")
        line.append(str(row[3]))
        line.append(str(row[4]))
        line.append(str(row[5]))
        line.append(" ")
        line.append(str(row[6]))
        line.append(str(row[7]))
        line.append(str(row[8]))
        line.append(" ")

        print(''.join(line))

def next_empty(puz):

    for i in range(0, 9):

        for j in range(0, 9):

            #print("Checking if (" + str(i) + ", " + str(j) + ") is empty")

            if puz[i][j] == 0:

                return (i, j)

    return (-1, -1)

def sq_valid(puz, num, row, col, b):
    
    #Check along row

    for c in range(9):

        if puz[row][c] == num:

            return False

    #Check along column

    for r in range(9):

        if puz[r][col] == num:

            return False

    #Check within box

    box_i = 0
    current_box = None

    #print("Establishing current box")
    
    while current_box == None:

        #print("Checking if " + str((row,col)) + " in " + str(b[box_i]))

        if (row, col) in b[box_i]:
            current_box = box_i
        else:
            box_i += 1

        #print("Current box: " + str(current_box))

    for b_point in b[current_box]:

        #Ignore current square
        if b_point != (row,col):

            if puz[b_point[0]][b_point[1]] == num:

                return False

    return True

def solve(puz, b):

    global total
    
    current_square = next_empty(puz)

    if current_square == (-1,-1):

        print("Solved!")
        print_puz(puz)

        result = int(str(puz[0][0]) + str(puz[0][1]) + str(puz[0][2]))
        
        total += result
        
        return True

    

    for n in range(1, 10):

        if sq_valid(puz, n, current_square[0], current_square[1], b):

            puz[current_square[0]][current_square[1]] = n

            if solve(puz, b):
                return True

            puz[current_square[0]][current_square[1]] = 0

    return False


boxes = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b8 = []
b9 = []

for i in range(9):

    for j in range(9):
        
        point = (i, j)

        if i <= 2 and j <= 2:
            b1.append(point)

        elif i > 2 and i <= 5 and j <= 2:
            b2.append(point)

        elif i > 5 and j <= 2:
            b3.append(point)

        elif i <= 2 and j > 2 and j <= 5:
            b4.append(point)

        elif i > 2 and i <= 5 and j > 2 and j <= 5:
            b5.append(point)

        elif i > 5 and j > 2 and j <= 5:
            b6.append(point)

        elif i <= 2 and j > 5:
            b7.append(point)

        elif i > 2 and i <= 5 and j > 5:
            b8.append(point)

        elif i > 5 and j > 5:
            b9.append(point)

boxes.append(b1)
boxes.append(b2)
boxes.append(b3)
boxes.append(b4)
boxes.append(b5)
boxes.append(b6)
boxes.append(b7)
boxes.append(b8)
boxes.append(b9)

f = open("p096_sudoku.txt")

tmp1 = f.readlines()
f.close()

allp = []
current = []

for tm in tmp1:

    this_line = tm.replace("\n", "")

    this_line_list = list(this_line)

    this_line_num = []

    if 'G' in this_line_list:
        this_line_num = ['G']
    else:
    
        for char in this_line_list:

            this_line_num.append(int(char))

    
    if 'G' in this_line_num:
        allp.append(current)
        current = []
    else:
        current.append(this_line_num)


allp.append(current)

d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del allp[0]

puzzle = allp[0]

#puzzle[row][col]

for puzzle in allp:

    solve(puzzle, boxes)

#print(sq_valid(puzzle, 5, 0, 0, boxes))


print("----------")
print("Total = " + str(total))
    
    
