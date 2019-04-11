#euler 107
#259679


import copy

def find_largest(gr, to_ignore):
	largest = 0
	
	i = 0
	j = 0		
	
	while i < len(gr):
		
		j = 0
		
		while j < len(gr[i]):
			
			if gr[i][j] > largest:
				if (i,j) not in to_ignore:
					largest = gr[i][j]
					to_del_i = i
					to_del_j = j
			
			j += 1
			
		i += 1
	
	return largest, to_del_i, to_del_j
	

def delete_largest_edge2(gr):
	
	done = False
	ignore = []
	
	while not done:
	
		largest, di, dj = find_largest(gr, ignore)
		
		graph_copy = copy.deepcopy(gr)
		
		print("Attempting to delete " + str(graph_copy[di][dj]))
		
		graph_copy[di][dj] = -1
		graph_copy[dj][di] = -1
		
		if spanning(graph_copy):
			done = True
			print("Deleted successfully")
			return True, graph_copy
		else:
			ignore.append((di,dj))
			print("Failed to delete without breaking graph, ignoring")
			
			if len(ignore) == len(gr):

				print("No edge can be deleted without breaking apart the network")
				return False, gr
			
		
	print("\nDeleting " + str(gr[to_del_i][to_del_j]) + "\n")
	
	gr[to_del_i][to_del_j] = -1
	gr[to_del_j][to_del_i] = -1

def weight(gr):
	t = 0
		
	for row in gr:
		for r in row:
			if r != -1:
				t += r
		
	return int(t/2)

def delete_largest_edge(gr):
	largest = 0
	
	i = 0
	
	while i < len(gr):
		
		j = 0
		
		while j < len(gr[i]):
			
			if gr[i][j] > largest:
				largest = gr[i][j]
				to_del_i = i
				to_del_j = j
			
			j += 1
			
		i += 1
	
	print("\nDeleting " + str(gr[to_del_i][to_del_j]) + "\n")
	
	gr[to_del_i][to_del_j] = -1
	gr[to_del_j][to_del_i] = -1
	

def print_graph(graph):
	for g in graph:
		print(g)
		
def del_edge(node, edge, gr):
	ind = gr[node].index(edge)
	gr[node][ind] = -1
	gr[ind][node] = -1

def connected_edges(nodes, gr, vis):
	results = []
	
	for n in nodes:
		all_connected_edges = gr[n]
		for ce in all_connected_edges:
			if ce != -1: 
				results.append((all_connected_edges.index(ce), ce))
			
	return results 

def connected_nodes(node, gr):
	output = []
	for i, g in enumerate(gr[node]):
		if g != -1:
			output.append(i)
			
	return output


def connected_node_with_shortest_edge(node, gr, vis):
	con_edges = connected_edges([node], gr, vis)
	#for ce in con_edges:
		


def shortest_edge(node, gr, vis):
	shortest = -1
	
	print("Finding shortest edge. Looking at edges: " + str(connected_edges([node], gr, vis)))
	
	for nod, ed in connected_edges([node], gr, vis):
		
			if ed < shortest and ed != 0:
				shortest = ed
				node_with_shortest = nod
	
	return shortest, node_with_shortest

def dfs(graph1, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph1[node]:
            dfs(graph1,n, visited)
    return visited

def spanning(gr):
	
	tree = {}

	all_nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

	for i, g in enumerate(gr):
		tree[i] = []
	
	for key, row in enumerate(gr):
		for v in row:
		
			if v != -1:
				tree[key].append(row.index(v))
	
	for j in range(0, 40):
	
		vis = dfs(tree, j, [])
		
		if sorted(list(set(vis))) != all_nodes:
			return False
		
	return True	
		
		
			

f = open("p107_network.txt")

all_text = f.readlines()
f.close()

graph = []


for a in all_text:
	line1 = a.replace('\n', '')
	line2 = line1.split(',')
	
	new_line = []
	
	for l in line2:
		if l == '-':
			new_line.append(-1)
		else:
			new_line.append(int(l))
	
	graph.append(new_line)
	
	#print(line)


	
#Each row represents a vertex 

orig_total = weight(graph)

print("Original total weight: " + str(orig_total))	

final_weight = 0
visited = []
current_node = 0
done = False

while not done:
	

	status, graph = delete_largest_edge2(graph)	
	
	print("Current difference: " + str(orig_total - weight(graph)))
	#input()
	
	#print_graph(last_graph)
	#print()

	if not status:
		print("Solution done")
		
		
		total = weight(graph)
		print("New total weight: " + str(total))
		
		print("Difference: " + str(orig_total-total))
		#do something with last_graph
		done = True


	
	
	