DOWN = (0,1)
UP = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

def move(cur_direction, tile):
	if tile == '|':
		if cur_direction == DOWN or cur_direction == UP:
			return cur_direction
		return (0,0)
	if tile == '-':
		if cur_direction == LEFT or cur_direction == RIGHT:
			return cur_direction
		return (0,0)
	if tile == 'L':
		if cur_direction == DOWN:
			return RIGHT
		elif cur_direction == LEFT:
			return UP
		return (0,0)
	if tile == 'J':
		if cur_direction == DOWN:
			return LEFT
		elif cur_direction == RIGHT:
			return UP
		return (0,0)
	if tile == '7':
		if cur_direction == UP:
			return LEFT
		elif cur_direction == RIGHT:
			return DOWN
		return (0,0)
	if tile == 'F':
		if cur_direction == UP:
			return RIGHT
		elif cur_direction == LEFT:
			return DOWN
		return (0,0)
	if tile == '.':
		return (0,0)


with open('data.txt', 'r') as f:
	tiles = [x.strip() for x in f.readlines()]
	start_x, start_y = 0,0
	for i,line in enumerate(tiles):
		if line.find('S') > -1:
			start_x = line.find('S')
			start_y = i
			break

	new_tiles = [['.' for x in ytiles]for ytiles in tiles]

	start_pos = (start_y,start_x)
	new_tiles[start_y][start_x] = 'S'
	direction = LEFT
	pos = (start_y, start_x-1)
	i = 1
	new_tiles[pos[0]][pos[1]] = tiles[pos[0]][pos[1]]

	while pos != start_pos:
		direction = move(direction, tiles[pos[0]][pos[1]])
		pos = (pos[0]+direction[1], pos[1]+direction[0])
		i += 1
		new_tiles[pos[0]][pos[1]] = tiles[pos[0]][pos[1]]

	print('Part 1: ', i//2)
	new_tiles[start_pos[0]][start_pos[1]] = '7'	# Our S is a 7. Hårdkodning är livet!
	walls = {'L':0,'J':0,'|':0}
	i = 0
	for row in new_tiles:
		j = 0
		for tile in row:
			if tile in walls:
				j += 1
			if tile == '.' and j % 2 == 1:
				i += 1
	print('Part 2: ', i)