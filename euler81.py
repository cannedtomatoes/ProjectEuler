#euler 81

import math

def print_grid(g):
    for l in g:
        print(l)
    print()

size = 80

#test = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
test = []

f = open("p081_matrix.txt")
all_lines = f.readlines()

for eachl in all_lines:
    
    line = eachl.strip().split(",")
    new_line = []
    
    for num in line:
        new_line.append(int(num))
    
    test.append(new_line)
    


seen = []

#new [row, col]

for search_length in range(1, size+1):



    for i in range(0, search_length):
    
        for j in range(0, search_length):
        
            if (i,j) not in seen:
                test_val = test[i][j]
                seen.append((i,j))
            
                up_added = -1
                left_added = -1
        
                #print("Looking at " + str(test_val))
        
                #add up
                if i > 0:
                    up_added = test_val + test[i-1][j]
        
                #add left
                if j > 0:
                    left_added = test_val + test[i][j-1]
           
                #print("Comparing to " + str(up_added) + " and " + str(left_added))   
           
                if up_added != -1 and left_added != -1:
                    lowest = min([up_added, left_added])
                elif up_added == -1 and left_added == -1:
                    lowest = test_val
                elif up_added == -1:
                    lowest = left_added
                elif left_added == -1:
                    lowest = up_added
                else:
                    print("Broke")
                    exit()
            
                test[i][j] = lowest
        
                #print("Setting (" + str(i) + ", " + str(j) + ") to " + str(lowest))
                #input()
    
            #print_grid(new)
        
print_grid(test)
