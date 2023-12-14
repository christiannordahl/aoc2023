import re

with open('data.txt', 'r') as f:
	lines = [line.rstrip() for line in f.readlines()]
	total_number = 0
	sum_gear_ratio = 0

	symbol_pattern = r"[^a-zA-Z0-9\.\n]+"
	number_pattern = r"[\d]+"
	star_pattern = r"\*"

	before = []
	current = []
	number_indices_before = []
	number_indices = []
	numbers_before = []
	numbers = []
	after = [x for m in re.finditer(symbol_pattern, lines[0]) for x in range(m.start(0), m.end(0))]
	number_indices_after = [[x for x in range(m.start(0)-1, m.end(0)+1)] for m in re.finditer(number_pattern, lines[0])]
	numbers_after = [int(m) for m in re.findall(number_pattern, lines[0])]

	for i in range(len(lines)-1):
		# Part 1
		before, current = current, after
		number_indices_before, number_indices = number_indices, number_indices_after
		numbers_before, numbers = numbers, numbers_after

		after = [x for m in re.finditer(symbol_pattern, lines[i+1]) for x in range(m.start(0), m.end(0))]
		number_indices_after = [[x for x in range(m.start(0)-1, m.end(0)+1)] for m in re.finditer(number_pattern, lines[i+1])]
		numbers_after = [int(m) for m in re.findall(number_pattern, lines[i+1])]
		special_set = set(before+current+after)

		for number_index, number in zip(number_indices, numbers):
			number_set = set(number_index)
			if special_set.intersection(number_set):
				#print(number, 'is set!')
				total_number += number

		# Part 2
		star_indices = [m.start(0) for m in re.finditer(star_pattern, lines[i])]
		for star_index in star_indices:
			collissions = 0
			number_list = []
			for number_index, number in zip(number_indices_before, numbers_before):
				if star_index in number_index:
					collissions += 1
					number_list.append(number)
			for number_index, number in zip(number_indices, numbers):
				if star_index in number_index:
					collissions += 1
					number_list.append(number)
			for number_index, number in zip(number_indices_after, numbers_after):
				if star_index in number_index:
					collissions += 1
					number_list.append(number)
			if collissions == 2:
				sum_gear_ratio += number_list[0]*number_list[1]



	# Part 1 - Final iteration
	number_indices = [[x for x in range(m.start(0)-1, m.end(0)+1)] for m in re.finditer(number_pattern, lines[-1])]
	numbers = [int(m) for m in re.findall(number_pattern, lines[-1])]
	special_set = set(current+after)

	for number_index, number in zip(number_indices, numbers):
		number_set = set(number_index)
		if special_set.intersection(number_set):
			total_number += number
	print('Part 1:', total_number)

	# Part 2 - Final iteration
	star_indices = [m.start(0) for m in re.finditer(star_pattern, lines[-1])]
	for star_index in star_indices:
		collissions = 0
		number_list = []
		for number_index, number in zip(number_indices, numbers):
			if star_index in number_index:
				collissions += 1
				number_list.append(number)
		for number_index, number in zip(number_indices_after, numbers_after):
			if star_index in number_index:
				collissions += 1
				number_list.append(number)
		if collissions == 2:
			sum_gear_ratio += number_list[0]*number_list[1]
	print('Part 2:', sum_gear_ratio)
