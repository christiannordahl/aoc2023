with open('data.txt', 'r') as f:
	lines = f.readlines()
	sum = 0
	
	# Part 1
	for line in lines:
		number = 0
		for x in line:
			if x.isdigit():
				number = int(x)*10
				break
		for x in line[::-1]:
			if x.isdigit():
				number += int(x)
				break

		sum += number

	print(sum)

	# Part 2
	values = 	['zero', 'one', 'two', 'three', 
				'four', 'five', 'six', 'seven', 
				'eight', 'nine', '0', '1', '2', 
				'3', '4', '5', '6', 
				'7', '8', '9']
	keys = 	{'zero': 0, 'one': 1, 'two': 2, 'three': 3,
				'four': 4, 'five': 5, 'six': 6, 'seven': 7, 
				'eight': 8, 'nine': 9, '0': 0, '1': 1, '2': 2, 
				'3': 3, '4': 4, '5': 5, '6': 6, 
				'7': 7, '8': 8, '9': 9}

	sum = 0
	i = 0
	for line in lines:
		first = len(line)
		first_key = 0
		last = -1
		last_key = 0
		for value in values:
			idx = line.find(value)
			if idx > -1 and idx < first:
				first = idx
				first_key = value
			idx = line.rfind(value)
			if idx > last:
				last = idx
				last_key = value
		sum += 10*keys[first_key] + keys[last_key]
		i += 1
	print(sum)