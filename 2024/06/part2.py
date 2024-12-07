import sys

def in_range(pos, size):
	return pos[0] >= 0 and pos[0] < size[0] and pos[1] >= 0 and pos[1] < size[1]


def move(pos, dir):
	return (pos[0] + dir[0], pos[1] + dir[1])


def rotate(dir):
	return (-dir[1], dir[0])


def is_cycled(pos, dir, map):
	size = (len(map[0]), len(map))

	visited = set()
	while True:
		if (pos, dir) in visited:
			return True
		
		visited.add((pos, dir))

		while True:
			next_pos = move(pos, dir)
			
			if not in_range(next_pos, size):
				return False

			if map[next_pos[1]][next_pos[0]] != "#":
				break

			dir = rotate(dir)

		pos = next_pos

def get_start(map):
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == "^":
				return (x, y)

def main():
	map = [list(line.strip()) for line in sys.stdin]

	size = (len(map[0]), len(map))

	result = 0

	pos = get_start(map)
	dir = (0, -1)

	while True:
		map[pos[1]][pos[0]] = "+"

		while True:
			next_pos = move(pos, dir)

			if not in_range(next_pos, size):
				print(result)
				return

			if map[next_pos[1]][next_pos[0]] != "#":
				break

			dir = rotate(dir)

		if map[next_pos[1]][next_pos[0]] != "+":
			map[next_pos[1]][next_pos[0]] = "#"
			result += is_cycled(pos, dir, map)

		pos = next_pos



if __name__ == "__main__":
	main()