#euler 816

import math
import itertools
from tqdm import tqdm

def adj_points(c_point):

        output = []

        cx = c_point[0]
        cy = c_point[1]

        output.append((cx-1, cy-1))
        output.append((cx, cy-1))
        output.append((cx+1, cy-1))

        output.append((cx-1, cy))
        output.append((cx, cy))
        output.append((cx+1, cy))

        output.append((cx-1, cy+1))
        output.append((cx, cy+1))
        output.append((cx+1, cy+1))

        return output

def shortest_dist(ps):

        dists = []

        for comb in itertools.combinations(ps, 2):

                point1 = comb[0]
                point2 = comb[1]

                x1 = point1[0]
                y1 = point1[1]
                x2 = point2[0]
                y2 = point2[1]
                
                this_dist = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))

                dists.append(this_dist)

        return min(dists)
                
                
# Function to round a point to the nearest grid point
def round_to_grid(point, d):

        x, y = point
        rounded_x = d * round(x / d)
        rounded_y = d * round(y / d)

        return (rounded_x, rounded_y)

        

def gens():

        output = 290797

        while True:

                yield output

                output = (output*output) % 50515093
s = []
count = 1
highest = 2000000
#highest = 14

print("Starting")

for g in gens():

        s.append(g)

        if count < highest*2:
                count += 1
        else:
                break

points = []

grid_points = {}

print("Generating points")

for n in range(0, highest):

        points.append((s[2*n], s[(2*n)+1]))

        this_point = (s[2*n], s[(2*n)+1])
        
        points.append(this_point)

#grid size
#d = 10000000
#d = 5000000
#d = 2500000
#d = 12500000
d = 700000

for p in tqdm(points):

        rounded_p = round_to_grid(p, d)

        if rounded_p not in grid_points:

                grid_points[rounded_p] = []
                
        
        grid_points[rounded_p].append(p)

#print(grid_points)
for k, v in grid_points.items():

        grid_points[k] = set(grid_points[k])

lowest = math.inf

#print("Checking", len(grid_points), "points")

for key, value in tqdm(grid_points.items()):
        
        if len(value) > 1:

                #print("Checking", len(value), "numbers from", key)

                dist = shortest_dist(value)

                if dist < lowest:

                        lowest = dist

print(lowest)
                
                

 
