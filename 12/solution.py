import re
from functools import lru_cache

def p1(dots, groups):
	if len(dots) == 0:
		if len(groups) == 0:
			return 1
		return 0
	if dots.startswith('.'):
		return p1(dots.strip('.'), groups)
	if dots.startswith('?'):
		return p1(dots.replace('?','.',1), groups) + p1(dots.replace('?','#',1), groups)
	if dots.startswith('#'):
		if len(groups) == 0:
			return 0
		if len(dots) < groups[0]:
			return 0
		if any('.' in x for x in dots[0:groups[0]]):
			return 0

		if len(groups) > 1:
			if len(dots) < groups[0]+1 or dots[groups[0]] == "#":
				return 0
			return p1(dots[groups[0]+1:], groups[1:])
		return p1(dots[groups[0]:], groups[1:])

@lru_cache
def p2(dots, groups):
	if len(dots) == 0:
		if len(groups) == 0:
			return 1
		return 0
	if dots.startswith('.'):
		return p2(dots.strip('.'), groups)
	if dots.startswith('?'):
		return p2(dots.replace('?','.',1), groups) + p2(dots.replace('?','#',1), groups)
	if dots.startswith('#'):
		if len(groups) == 0:
			return 0
		if len(dots) < groups[0]:
			return 0
		if any('.' in x for x in dots[0:groups[0]]):
			return 0

		if len(groups) > 1:
			if len(dots) < groups[0]+1 or dots[groups[0]] == "#":
				return 0
			return p2(dots[groups[0]+1:], groups[1:])
		return p2(dots[groups[0]:], groups[1:])

with open('data.txt', 'r') as f:
	total = 0
	for line in f.readlines():
		line = line.strip().split()
		left = re.sub(r'\.+', '.',line[0])
		right = [int(x) for x in line[1].split(',')]
		total += p1(left, right)
	print(total)

	# The @cache activates memoization
	# Have to use tuples instead of list
	f.seek(0)
	total = 0
	for line in f.readlines():
		line = line.strip().split()
		left = re.sub(r'\.+', '.',line[0])
		left = "?".join([left]*5)
		right = tuple([int(x) for x in line[1].split(',')])	# do a tuple instead of list
		right = right*5

		total += p2(left, right)
	print(total)