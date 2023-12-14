with open('data.txt', 'r') as f:
	times = list(map(int, f.readline().split(':')[1].split()))
	distances = list(map(int, f.readline().split(':')[1].split()))
	
	total_product = 1
	for time, distance in zip(times, distances):
		num_ways = 0
		for holding_time in range(1, time):	# Holding time is the same as speec
			race_time = time-holding_time
			if race_time*holding_time > distance:
				num_ways += 1
		if num_ways > 0:
			total_product*=num_ways

	print(total_product)
	# Part 2
	time = int(''.join([str(x) for x in times]))
	distance = int(''.join([str(x) for x in distances]))

	num_ways = 0
	for holding_time in range(1, time):	# Holding time is the same as speec
		race_time = time-holding_time
		if race_time*holding_time > distance:
			num_ways += 1

	print(num_ways)