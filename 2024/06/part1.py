import sys

def main():
	obstacles = set()

	for y, line in enumerate(sys.stdin):
		max_y = y
		for x, tile in enumerate(line.strip()):
			max_x = x
			if tile == "#":
				obstacles.add((x, y))
			elif tile == "^":
				pos = (x, y)

	dir = (0, -1)

	visited = set()
	while not (pos[0] < 0 or pos[0] > max_x or pos[1] < 0 or pos[1] > max_y):
		visited.add(pos)
		
		while (pos[0] + dir[0], pos[1] + dir[1]) in obstacles:
			dir = (-dir[1], dir[0])

		pos = (pos[0] + dir[0], pos[1] + dir[1])


	print(len(visited))


if __name__ == "__main__":
	main()