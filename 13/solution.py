def p1_pattern_matcher(pattern):
	for i in range(len(pattern)-1):
		if pattern[i] == pattern[i+1]:
			for j in range(i+1):
				if i+1+j < len(pattern):
					if pattern[i+1+j] != pattern[i-j]:
						break
			else:
				num_rows = i+1
				break
	else:
		return False,0
	return True, num_rows

def p2_pattern_matcher(pattern):
	for i in range(len(pattern)-1):
		smudge_removed = False
		diff_indices = [x for x in range(len(pattern[i])) if pattern[i][x] != pattern[i+1][x]]
		if pattern[i] == pattern[i+1] or len(diff_indices) == 1:
			if len(diff_indices) == 1:
				smudge_removed = True
			for j in range(1,i+1):
				if i+1+j < len(pattern):
					if pattern[i+1+j] != pattern[i-j]:
						diff_indices = [x for x in range(len(pattern[i+1+j])) if pattern[i+1+j][x] != pattern[i-j][x]]
						if len(diff_indices) > 1 or smudge_removed == True:
							break
						smudge_removed = True
			else:
				if smudge_removed == True:
					num_rows = i+1
					break
	else:
		return False,0
	return True,num_rows

with open('data.txt', 'r') as f:
	patterns = [[line.strip() for line in patterns.split('\n')] for patterns in ''.join(f.readlines()).split('\n\n')]

	# Part 1
	total_sum = 0
	for pattern in patterns:
		answer, num_rows = p1_pattern_matcher(pattern)
		if answer:
			total_sum += 100*num_rows
			continue

		# Transposes pattern, Easier to use == and !=
		pattern = [''.join(s) for s in zip(*pattern)]
		answer, num_cols = p1_pattern_matcher(pattern)
		if answer:
			total_sum += num_cols
		
	print(total_sum)

	# Part 2

	total_sum = 0
	for pattern in patterns:
		answer, num_rows = p2_pattern_matcher(pattern)
		if answer:
			total_sum += 100*num_rows
			continue

		pattern = [''.join(s) for s in zip(*pattern)]
		answer, num_cols = p2_pattern_matcher(pattern)
		if answer:
			total_sum += num_cols

	print(total_sum)






