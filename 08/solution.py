with open('data.txt', 'r') as f:
	instructions = f.readline().rstrip()
	f.readline()

	nodes = {}
	for line in f.readlines():
		node,path = line.rstrip().split(' = ')
		path = path[1:-1].split(', ')
		nodes[node] = {}
		nodes[node]['L'] = path[0]
		nodes[node]['R'] = path[1]

	# # Part 1
	i = 0
	current = 'AAA'
	while current != 'ZZZ':
		if instructions[i%len(instructions)] == 'L':
			current = nodes[current]['L']
		else:
			current = nodes[current]['R']

		i += 1
	print(i)

	# Part 2
	start_nodes = [x for x in nodes.keys() if x.endswith('A')]

	from math import lcm
	i = 0
	current_nodes = start_nodes
	cycles = []
	while True:
		for j in range(len(current_nodes)):
			if instructions[i%len(instructions)] == 'L':
				current_nodes[j] = nodes[current_nodes[j]]['L']
			else:
				current_nodes[j] = nodes[current_nodes[j]]['R']
			if current_nodes[j].endswith('Z'):
				cycles.append(i+1)
		if len(cycles) == len(start_nodes):
			break
		i += 1

	print(lcm(*cycles))