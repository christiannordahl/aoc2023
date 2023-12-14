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
		maps.append(read_and_map_part_2(f))
	maps.reverse()

	location = 45
	while True:
		location += 1
		possible_seed = location
		for mapp in maps:
			for mappp in mapp:
				if mappp[0] <= possible_seed < mappp[1]:
					possible_seed += mappp[2]
					break

		for seed_ranges in seeds:
			if seed_ranges[0] <= possible_seed < seed_ranges[1]:
				break
		else:
			continue
		break
	print(location)

	# Part 2 - Proper way
	# Identify the proper mapping, bottom up.
	# See which range produces the lowest score and if you can sneak through below it. 
	# Keep track of those two and keep going up.
	# The range from each step should be [0, minimum_seed) [minimum_seed, maximum_seed)
	# First identify the range minimum_seed, maximum_seed, then use the minimum seeds 
	# to determine the possible sneaking that will be better than that. Then just compare against seeds
	
