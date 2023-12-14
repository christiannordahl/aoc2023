import re

def add_to_path(source, destination, row_voids, column_voids):
	sum_addition = 0

	for row_void in row_voids:
		if source[0] <= row_void <= destination[0]:
			sum_addition += 999999
		elif source[0] >= row_void >= destination[0]:
			sum_addition += 999999
	for column_void in column_voids:
		if source[1] <= column_void <= destination[1]:
			sum_addition += 999999
		elif source[1] >= column_void >= destination[1]:
			sum_addition += 999999

	return sum_addition

with open('data.txt', 'r') as f:
	lines = [line.strip() for line in f]

	new_lines = []
	for line in lines:
		if line == len(line) * line[0]:
			new_lines.append(line)
		new_lines.append(line)
	lines = [''.join(s) for s in zip(*new_lines)]
	new_lines = []
	for line in lines:
		if line == len(line) * line[0]:
			new_lines.append(line)
		new_lines.append(line)
	lines = new_lines

	galaxies = []
	for i in range(len(lines)):
		coordinates = [m.start(0) for m in re.finditer(r"#", lines[i])]
		for coordinate in coordinates:
			galaxies.append([i,coordinate])

	sum_distances = 0
	for i,source in enumerate(galaxies[:-1]):
		for destination in galaxies[i:]:
			sum_distances += (abs(source[0]-destination[0])) + (abs(source[1]-destination[1]))
	print(sum_distances)

	# Part 2
	f.seek(0)
	lines = [line.strip() for line in f]
	galaxies = []
	for i in range(len(lines)):
		coordinates = [m.start(0) for m in re.finditer(r"#", lines[i])]
		for coordinate in coordinates:
			galaxies.append([i,coordinate])

	column_voids = []
	row_voids = []
	for i,line in enumerate(lines):
		if line == len(line) * line[0]:
			row_voids.append(i)
	lines = [''.join(s) for s in zip(*lines)]
	for i,line in enumerate(lines):
		if line == len(line) * line[0]:
			column_voids.append(i)
	lines = [''.join(s) for s in zip(*lines)]

	sum_distances = 0
	for i,source in enumerate(galaxies[:-1]):
		for destination in galaxies[i:]:
			sum_distances += (abs(source[0]-destination[0])) + (abs(source[1]-destination[1]))
			sum_distances += add_to_path(source, destination, row_voids, column_voids)
	
	print(sum_distances)