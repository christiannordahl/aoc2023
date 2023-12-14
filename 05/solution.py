def read_and_map(f):
	lst = []
	while True:
		line = f.readline()
		if line == '\n' or line == '':
			break
		line = [int(x) for x in line.rstrip().split()]
		lst.append([line[1], line[1]+line[2], line[1]-line[0]])
	return lst

def read_and_map_part_2(f):
	values = []
	while True:
		line = f.readline()
		if line == '\n' or line == '':
			break
		line = line.split()
		values.append([int(line[0]),int(line[0])+int(line[2]),int(line[1])-int(line[0])])
	
	return values

def read_and_map_part_2_2(f):
	values = []
	while True:
		line = f.readline()
		if line == '\n' or line == '':
			break
		line = line.split()
		values.append([int(line[1]),int(line[1])+int(line[2]),int(line[1])-int(line[0])])
	
	return values

with open('data.txt', 'r') as f:
	seeds = [int(x) for x in f.readline().rstrip().split(':')[1].lstrip().split()]
	maps = []
	f.readline()

	for i in range(7):
		f.readline()
		maps.append(read_and_map(f))

	# Part 1
	best_loc = None
	best_seed = None
	for seed in seeds:
		current_index = seed
		for mapp in maps:
			for mappp in mapp:
				if mappp[0] <= current_index <= mappp[1]:
					current_index -= mappp[2]
					break
			else:	# Do we need to do something if we don't find it?
				current_index = current_index	# placeholder
		if best_loc is None or current_index < best_loc:
			best_loc = current_index

	print(best_loc)

	#Part 2 - brute force, will work but is slow.
	# new_seeds = []
	# for i in range(0, len(seeds), 2):
	# 	new_seeds.extend([x for x in range(seeds[i],seeds[i]+seeds[i+1])])
	# seeds = new_seeds
	# best_seed = None
	# for seed in seeds:
	# 	current_index = seed
	# 	for mapp in maps:
	# 		for mappp in mapp:
	# 			if mappp[0] <= current_index <= mappp[1]:
	# 				current_index -= mappp[2]
	# 				break
	# 		else:	# Do we need to do something if we don't find it?
	# 			current_index = current_index	# placeholder
	# 	if best_loc is None or current_index < best_loc:
	# 		best_loc = current_index
	# print(best_loc)

# with open('data.txt', 'r') as f:

# 	seeds = [int(x) for x in f.readline().strip().split(':')[1].split()]
# 	new_seeds = []
# 	for i in range(0, len(seeds), 2):
# 		new_seeds.append([seeds[i],seeds[i]+seeds[i+1]])
# 	seeds = new_seeds

# 	maps = []
# 	f.readline()
# 	for i in range(7):
# 		f.readline()
# 		maps.append(read_and_map_part_2(f))
# 	maps.reverse()

# 	location = 0
# 	while True:
# 		location += 1
# 		possible_seed = location
# 		for mapp in maps:
# 			for mappp in mapp:
# 				if mappp[0] <= possible_seed < mappp[1]:
# 					possible_seed += mappp[2]
# 					break

# 		for seed_ranges in seeds:
# 			if seed_ranges[0] <= possible_seed < seed_ranges[1]:
# 				break
# 		else:
# 			continue
# 		break
# 	print(location)

from queue import Queue

def traverse_mapping(seed, maps):
	if len(maps) == 0:
		return seed[0]
	q = Queue()
	q.put(seed)
	best_location = -1
	while not q.empty():
		seed = q.get()
		for mapp in maps[0]:
			if mapp[0] <= seed[0] and seed[1] < mapp[1]:	# Entire seed range fits in mapping
				new_location = traverse_mapping([seed[0]-mapp[2],seed[1]-mapp[2]],maps[1:])
				break
			elif mapp[0] <= seed[0] < mapp[1]:				# Seed range starts in mapping, ends afterwards
				i = mapp[1] - seed[0]
				q.put([mapp[1],seed[1]])
				new_location = traverse_mapping([seed[0]-mapp[2],mapp[1]-mapp[2]], maps[1:])
				break
			elif mapp[0] < seed[1] < mapp[1]:				# Seed range ends in mapping, starts before.
				i = seed[1] - mapp[0]
				q.put([seed[0], mapp[0]])					# Put the range before mapping back into queue
				new_location = traverse_mapping([mapp[0]-mapp[2], seed[1]-mapp[2]], maps[1:])
				break
		else:												# If we could not map the range, we just pass it along
			new_location = traverse_mapping(seed, maps[1:])

		if best_location == -1 or new_location < best_location:
			best_location = new_location
	return best_location

with open('data.txt', 'r') as f:
	seeds = [int(x) for x in f.readline().strip().split(':')[1].split()]
	new_seeds = []
	for i in range(0, len(seeds), 2):
		new_seeds.append([seeds[i],seeds[i]+seeds[i+1]])
	seeds = new_seeds

	maps = []
	f.readline()
	for i in range(7):
		f.readline()
		maps.append(read_and_map_part_2_2(f))

	min_location = 98712398712398712398172398712398172391827391283719283719823719827391
	for seed in seeds:
		location = traverse_mapping(seed, maps)
		if location < min_location:
			min_location = location
	print(min_location)
		
	
