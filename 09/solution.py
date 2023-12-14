with open('data.txt', 'r') as f:
	total_post_extrapolated = 0
	total_pre_extrapolated = 0
	for line in f:
		data = []
		data = list(map(int, line.strip().split()))
		differences = []

		# Part 1
		differences.append([data[i+1]-data[i] for i in range(len(data)-1)])
		while True:
			if sum(differences[-1]) == 0:
				break
			differences.append([differences[-1][i+1]-differences[-1][i] for i in range(len(differences[-1])-1)])

		differences[-1].append(0)
		for i in range(len(differences)-2, -1, -1):
			differences[i].append(differences[i][-1]+differences[i+1][-1])
		total_post_extrapolated += data[-1]+differences[0][-1]

		# Part 2
		pre_extrapolated = 0
		for i in range(len(differences)-2,-1,-1):
			pre_extrapolated = differences[i][0]-pre_extrapolated
		total_pre_extrapolated += data[0]-pre_extrapolated

	print(total_post_extrapolated)
	print(total_pre_extrapolated)