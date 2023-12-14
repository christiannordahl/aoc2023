from functools import cmp_to_key

def rank_hand_pt1(item):
	# Identify which hand is present for both
	# Five of a kind	7
	# Four of a kind	6
	# Full House		5
	# Three of a kind	4
	# Two pairs			3
	# One Pair			2
	# High card			1
	keys = list(item.keys())
	if len(keys) == 1:	# If only one card exists, we have 5 of a kind
		return 7
	if len(keys) == 2:	# The two card combos
		if item[keys[0]] == 1 or item[keys[0]] == 4:	# Four of a kind
			return 6
		#if item[key[0]] == 3 or item[key[0]] == 2:	# Full house
		return 5
	if len(keys) == 3:
		if 3 in item.values():
			return 4
		#if item.values().count(2) == 2:
		return 3
	if list(item.values()).count(2) == 1:
		return 2
	return 1

def rank_hand_pt2(item, num_jokers):
	# Identify which hand is present for both
	# Five of a kind	7
	# Four of a kind	6
	# Full House		5
	# Three of a kind	4
	# Two pairs			3
	# One Pair			2
	# High card			1
	keys = list(item.keys())
	if len(keys) == 1:	# If only one card exists, we have 5 of a kind
		return 7
	if len(keys) == 2:	# The two card combos
		if num_jokers > 0:	# If joker(s) is present, it is 5 of a kind
			return 7
		if item[keys[0]] == 1 or item[keys[0]] == 4:	# Four of a kind
			return 6
		#if item[key[0]] == 3 or item[key[0]] == 2:	# Full house
		return 5
	if len(keys) == 3:
		if 3 in item.values():
			if num_jokers > 0:
				return 6
			return 4
		if list(item.values()).count(2) == 2:
			if num_jokers == 2:
				return 6
			if num_jokers == 1:
				return 5
		return 3
	if list(item.values()).count(2) == 1:
		if num_jokers > 0:
			return 4
		return 2
	if num_jokers > 0:
		return 2
	return 1

def compare_pt1(item1, item2):
	# First check
	item1 = item1[0]
	item2 = item2[0]
	counts1 = {x: item1.count(x) for x in list(set(item1))}
	counts2 = {x: item2.count(x) for x in list(set(item2))}

	rank1 = rank_hand_pt1(counts1)
	rank2 = rank_hand_pt1(counts2)

	# If someone has a better hand
	if rank1 != rank2:
		return rank2 - rank1

	# If they have equal hands
	# We replace the jack with an S to make it easier to compare
	# Now it is A > K > Q > S > T > 9 > 8 > ... > 0
	item1 = item1.replace('A', 'Z')
	item1 = item1.replace('K', 'Y')
	item1 = item1.replace('T', 'A')
	item1 = item1.replace('Q', 'X')
	item2 = item2.replace('A', 'Z')
	item2 = item2.replace('K', 'Y')
	item2 = item2.replace('T', 'A')
	item2 = item2.replace('Q', 'X')
	if item1 < item2:
		return 1
	if item2 < item1:
		return -1
	return 0
	
def compare_pt2(item1, item2):
	# First check
	item1 = item1[0]
	item2 = item2[0]
	counts1 = {x: item1.count(x) for x in list(set(item1))}
	counts2 = {x: item2.count(x) for x in list(set(item2))}
	num_jokers1 = item1.count('J')
	num_jokers2 = item2.count('J')

	rank1 = rank_hand_pt2(counts1, num_jokers1)
	rank2 = rank_hand_pt2(counts2, num_jokers2)

	# If someone has a better hand
	if rank1 != rank2:
		return rank2 - rank1

	# If they have equal hands
	# We replace the jack with an S to make it easier to compare
	# Now it is A > K > Q > S > T > 9 > 8 > ... > 0
	item1 = item1.replace('A', 'Z')
	item1 = item1.replace('K', 'Y')
	item1 = item1.replace('T', 'A')
	item1 = item1.replace('Q', 'X')
	item1 = item1.replace('J', '0')
	item2 = item2.replace('A', 'Z')
	item2 = item2.replace('K', 'Y')
	item2 = item2.replace('T', 'A')
	item2 = item2.replace('Q', 'X')
	item2 = item2.replace('J', '0')
	if item1 < item2:
		return 1
	if item2 < item1:
		return -1
	return 0

with open('data.txt', 'r') as f:
	rank_sum = 0
	data = [(x.split()[0], int(x.split()[1])) for x in f.readlines()]
	
	# Part 1
	data.sort(key=cmp_to_key(compare_pt1))
	rank = len(data)
	for dat in data:
		rank_sum += (dat[1]*rank)
		rank -= 1
	print(rank_sum)

	# Part 2
	rank_sum = 0
	data.sort(key=cmp_to_key(compare_pt2))
	rank = len(data)
	for dat in data:
		rank_sum += (dat[1]*rank)
		rank -= 1

	print(rank_sum)
