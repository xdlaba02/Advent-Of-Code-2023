import sys

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
					pos = (2 * a[0] - b[0], 2 * a[1] - b[1])

					if pos[0] >= 0 and pos[0] < size[0] and pos[1] >= 0 and pos[1] < size[1]:
						antinodes.add(pos)

	print(len(antinodes))

if __name__ == "__main__":
	main()
