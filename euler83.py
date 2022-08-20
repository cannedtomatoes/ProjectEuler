#euler82

import networkx as nx
import math

def int_row(row_list):

    output = []

    for ro in row_list:

        output.append(int(ro))

    return output

def path_weight(p):

    total = 0
    
    for e in p:

        total += e[0]

    return total

f = open("p083_matrix.txt")
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

        new_node = (rows[i][j], i, j)
        
        G.add_node(new_node)


        j += 1

    i += 1

#print(G.nodes())
#input()

#Add edges

i = 0
while i < size:

    j = 0
    
    while j <= size-1:

        current = (rows[i][j], i, j)

        #Get one above
        if i > 0:
            
            above = (rows[i-1][j], i-1, j)

            w = current[0] + above[0]
            
            G.add_edge(current, above, weight=w)
            #print(str(current) + " ^ " + str(above) + ", w = " + str(w))


   
        #Get one to the right
        if j < size-1:

            right = (rows[i][j+1], i, j+1)

            w = current[0] + right[0]
            
            G.add_edge(current, right, weight=w)
            #print(str(current) + " > " + str(right) + ", w = " + str(w))


        #Get one to the left
        if j > 0:

            left = (rows[i][j-1], i, j-1)

            w = current[0] + left[0]
            
            G.add_edge(current, left, weight=w)
            #print(str(current) + " < " + str(left) + ", w = " + str(w))

        #Get one below
        if i < size-1:
   
            below = (rows[i+1][j], i+1, j)

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

start = (rows[0][0], 0, 0)
goal = (rows[size-1][size-1], size-1, size-1)

        
#print("Start: " + str(left_pos) + ", End: " + str(right_pos))


path = nx.shortest_path(G, source=start, target=goal, weight='weight')

current_length = path_weight(path)            

    
print("Shortest: " + str(current_length))
print(path)










        
