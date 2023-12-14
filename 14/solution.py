def north_west(table):
	for i in range(len(table)):
		string = list(table[i])
		for j in range(1,len(table[i])):
			if string[j] == 'O':
				while j > 0 and string[j-1] != '#':
					string[j],string[j-1] = string[j-1],string[j]
					j -= 1
		table[i] = ''.join(string)

def south_east(table):
	for i in range(len(table)):
		string = list(table[i])
		for j in range(len(table)-2,-1, -1):
			if string[j] == 'O':
				while j < len(table)-1 and string[j+1] != '#':
					string[j],string[j+1] = string[j+1],string[j]
					j += 1
		table[i] = ''.join(string)

def score_table(table):
	total_sum = 0
	for i in range(len(table)):
		k = len(table[i])
		for j in range(len(table[i])):
			if table[i][j] == 'O':
				total_sum += (k-j)
	return total_sum

def rotate(table):
	table = [''.join(s) for s in zip(*table)]
	north_west(table)
	table = [''.join(s) for s in zip(*table)]
	north_west(table)
	table = [''.join(s) for s in zip(*table)]
	south_east(table)
	table = [''.join(s) for s in zip(*table)]
	south_east(table)
	return table

with open('data.txt', 'r') as f:

	table = [x.strip() for x in f.readlines()]
	table = [''.join(s) for s in zip(*table)]
	total_sum = 0

	# Part 1
	north_west(table)
	print(score_table(table))


	# Part 2
	total_sum = 0
	f.seek(0)
	table = [x.strip() for x in f.readlines()]
	prev_score = 1

	i = 0
	prev_tables = {}
	current_table = '\n'.join(table)
	for i in range(1, 1000000000):
		table = rotate(table)
		current_table = '\n'.join(table)
		if current_table in prev_tables:
			break
		prev_tables[current_table] = i
		i += 1

	current_index = i
	previous_index = prev_tables[current_table]

	iterations = (1000000000 - current_index) % (current_index - previous_index)

	for i in range(iterations):
		table = rotate(table)
	table = [''.join(s) for s in zip(*table)]
	print(score_table(table))