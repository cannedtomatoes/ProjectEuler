#euler82

import networkx as nx
import math

def int_row(row_list):

    output = []

    for ro in row_list:

        output.append(int(ro))

    return output

def format_node(x, y, s, r):

    if y == 0:
        #print("i = " + str(x) + ", j = " + str(y))
        #print("Returning " + str(r[x][y]) + ", L")
        return (r[x][y], 'L', x, y)
    elif y == s-1:
        #print("i = " + str(x) + ", j = " + str(y))
        #print("Returning " + str(r[x][y]) + ", R")
        return (r[x][y], 'R', x, y)
    else:
        #print("i = " + str(x) + ", j = " + str(y))
        #print("Returning " + str(r[x][y]) + ", None")
        return (r[x][y], None, x, y)

def path_weight(p):

    total = 0
    
    for e in p:

        total += e[0]

    return total

f = open("p082_matrix.txt")
#f = open("temp.txt")

li = f.readlines()

f.close()

rows = []

for l in li:

    temp1 = l.replace('\n', '')
    temp2 = temp1.replace(' ', '')
    row = temp2.split(",")    

    rows.append(int_row(row))

size = 80

i = 0
j = 0

d = {}
G = nx.DiGraph()

#add all nodes

left_wall = []
right_wall = []

i = 0

while i < size:

    j = 0
    
    while j < size:

        #print("Adding node at i = " + str(i) + ", j = " +str(j))

        new_node = format_node(i, j, size, rows)
        
        G.add_node(new_node)

        if new_node[1] == 'L':
            left_wall.append(new_node)
        elif new_node[1] == 'R':
            right_wall.append(new_node)


        j += 1

    i += 1

#print(G.nodes())
#input()

#Add edges

i = 0
while i < size:

    j = 0
    
    while j <= size-1:

        current = format_node(i, j, size, rows)

        #Get one above
        if i > 0:
            
            above = format_node(i-1, j, size, rows)

            w = current[0] + above[0]
            
            G.add_edge(current, above, weight=w)
            #print(str(current) + " ^ " + str(above) + ", w = " + str(w))


   
        #Get one to the right
        if j < size-1:

            right = format_node(i, j+1, size, rows)

            w = current[0] + right[0]
            
            G.add_edge(current, right, weight=w)
            #print(str(current) + " > " + str(right) + ", w = " + str(w))


        #Get one below
        if i < size-1:
   
            below = format_node(i+1, j, size, rows)

            w = current[0] + below[0]

            G.add_edge(current, below, weight=w)
            #print(str(current) + " v " + str(below) + ", w = " + str(w))


        j +=1
        

    i += 1

#print(G.edges())
#input()





shortest = math.inf
current_length = 0

print("Start search")

for left_pos in left_wall:


    for right_pos in right_wall:

        
        #print("Start: " + str(left_pos) + ", End: " + str(right_pos))
        

        path = nx.shortest_path(G, source=left_pos, target=right_pos, weight='weight')
        
        current_length = path_weight(path)            
        #print("Length: " + str(current_length))
        #print(path)
        #input()
            
        if current_length < shortest:
            shortest = current_length
            
            print("Shortest: " + str(current_length))
            #print(path)
    









        
