import sys


def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])


def search(track, symbol):
	for y in range(len(track)):
		for x in range(len(track[y])):
			if track[y][x] == symbol:
				return (x, y)


def main():
	track = [list(line.strip()) for line in sys.stdin]

	pos = search(track, "S")

	path = {}

	while True:
		path[pos] = len(path)

		if track[pos[1]][pos[0]] == "E":
			break

		for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			new_pos = add_tuples(pos, dir)
			if new_pos not in path and track[new_pos[1]][new_pos[0]] != "#":
				pos = new_pos
				break

	result = 0

	for pos, distance in path.items():
		for dir in [(1, 1), (-1, 1), (1, -1), (-1, -1), (2, 0), (0, 2), (-2, 0), (0, -2)]:
			new_pos = add_tuples(pos, dir)

			if new_pos in path:
				result += path[new_pos] - distance - 2 >= 100

	print(result)


if __name__ == "__main__":
	main()