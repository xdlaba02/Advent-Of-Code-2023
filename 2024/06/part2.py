import sys

def in_range(pos, max):
	return pos[0] >= 0 and pos[0] <= max[0] and pos[1] >= 0 and pos[1] <= max[1]


def move(pos, dir):
	return (pos[0] + dir[0], pos[1] + dir[1])


def rotate(dir):
	return (-dir[1], dir[0])


def is_cycled(pos, max, obstacles):
	dir = (0, -1)

	visited = set()
	while in_range(pos, max):
		if (pos, dir) in visited:
			return True
		
		visited.add((pos, dir))

		while move(pos, dir) in obstacles:
			dir = rotate(dir)

		pos = move(pos, dir)

	return False


def main():
	obstacles = set()

	for y, line in enumerate(sys.stdin):
		max_y = y
		for x, tile in enumerate(line.strip()):
			max_x = x
			if tile == "#":
				obstacles.add((x, y))
			elif tile == "^":
				starting_pos = (x, y)

	result = 0

	pos = starting_pos
	dir = (0, -1)

	visited = set()
	while in_range(pos, (max_x, max_y)):		
		visited.add(pos)

		while move(pos, dir) in obstacles:
			dir = rotate(dir)

		if move(pos, dir) not in visited:
			result += is_cycled(starting_pos, (max_x, max_y), obstacles.union({move(pos, dir)}))

		pos = move(pos, dir)

	print(result)


if __name__ == "__main__":
	main()