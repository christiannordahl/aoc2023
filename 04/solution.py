with open('data.txt', 'r') as f:
	lines = [line.rstrip() for line in f.readlines()]
	total_points = 0
	future_multipliers = [0]
	total_scratchcards = 0

	for line in lines:
		# Part 1
		winning_numbers, our_numbers = line.split('|')
		winning_numbers = [int(x) for x in winning_numbers.split(':')[1].lstrip().rstrip().split()]
		our_numbers = [int(x) for x in our_numbers.lstrip().rstrip().split()]
		
		count = 0
		for num in winning_numbers:
			count += our_numbers.count(num)

		points = 0
		if count > 0:
			points = 1
			for i in range(1,count):
				points *= 2
		total_points += points

		# Part 2
		multiplier = 0
		if len(future_multipliers) > 0:
			multiplier = future_multipliers.pop(0)

		if count > len(future_multipliers):
			for i in range(count-len(future_multipliers)):
				future_multipliers.append(0)

		for i in range(count):
			future_multipliers[i] += 1+multiplier

		total_scratchcards += 1+multiplier

	print('Part 1:', total_points)
	print('Part 2:', total_scratchcards)