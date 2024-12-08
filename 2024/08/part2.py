import sys

def pos_add(a, b):
	return (a[0] + b[0], a[1] + b[1])

def pos_diff(a, b):
	return (a[0] - b[0], a[1] - b[1])

def in_range(pos, size):
	return pos[0] >= 0 and pos[0] < size[0] and pos[1] >= 0 and pos[1] < size[1]

def main():
	map = [line.strip() for line in sys.stdin]

	size = (len(map[0]), len(map))

	antenas = {}

	for y, line in enumerate(map):
		for x, c in enumerate(line):
			if c != ".":
				antenas.setdefault(c, []).append((x, y))

	antinodes = set()

	for positions in antenas.values():
		for a in positions:
			for b in positions:
				if a != b:
					pos = b
					diff = pos_diff(b, a)
					while in_range(pos, size):
						antinodes.add(pos)
						pos = pos_add(pos, diff)

	print(len(antinodes))

if __name__ == "__main__":
	main()
