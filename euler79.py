#euler 79

def dead_end(graph):
	#finds any nodes that are a dead end 
	seen_nodes = []
	all_nodes = []
	for key, val in graph.items():
		for v in val:
			if v not in seen_nodes:
				seen_nodes.append(v)
			
		if key not in all_nodes:
			all_nodes.append(key)
			
	return list(set(all_nodes) - set(seen_nodes))[0]

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


entries_orig = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]
entries = []

for ent in entries_orig:
	entries.append(list(str(ent)))

graph = {}

for e in entries:
	
	#print("e = " + str(e))
	#print("e[0] = " + str(e[0]))
	#print("e[1] = " + str(e[1]))
	
	
	if e[0] not in graph:
		graph[e[0]] = [e[1]]
	else:
		if e[1] not in graph[e[0]]:
			graph[e[0]].append(e[1])
	
	#print("e = " + str(e))
	#print("e[1] = " + str(e[1]))
	#print("e[2] = " + str(e[2]))
	
			
	if e[1] not in graph:
		graph[e[1]] = [e[2]]
	else:
		if e[2] not in graph[e[1]]:
			graph[e[1]].append(e[2])


	#print(graph)
	#input()
highest = 0
			
for p in find_all_paths(graph, '3', '0'):
	if len(p) > highest:
		highest = len(p)
		result = p

result.insert(0, dead_end(graph))

#print(graph)
print(''.join(result))