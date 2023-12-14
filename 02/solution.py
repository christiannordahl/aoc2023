with open('data.txt', 'r') as f:
	lines = f.readlines()
	sum_game_nums = 0
	sum_power = 0
	for line in lines:
		game_number, data = line.split(':')
		game_number = int(game_number.split(' ')[1])
		rounds = data.split(';')
		max_cubes = {'blue': 0, 'green': 0, 'red': 0}
		for round in rounds:
			cubes = round.split(',')
			for cube in cubes:
				num = int(cube.lstrip().split(' ')[0])
				if 'blue' in cube:
					if max_cubes['blue'] < num:
						max_cubes['blue'] = num
				elif 'green' in cube:
					if max_cubes['green'] < num:
						max_cubes['green'] = num
				elif 'red' in cube:
					if max_cubes['red'] < num:
						max_cubes['red'] = num

		# Part 1
		if max_cubes['blue'] <= 14 and max_cubes['green'] <= 13 and max_cubes['red'] <= 12:
			sum_game_nums += game_number

		# Part 2
		power = 1
		for key in max_cubes.keys():
			power *= max_cubes[key]

		sum_power += power
	print('Part 1:', sum_game_nums)
	print('Part 2:', sum_power)

