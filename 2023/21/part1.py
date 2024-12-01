import sys

def main():
	map = [row.strip() for row in sys.stdin]

	width = len(map[0])
	height = len(map)

	positions = set()

	for y, row in enumerate(map):
		for x, c in enumerate(row):
			if c == "S":
				positions.add((x, y))

	for i in range(64):
		new_positions = set()
		
		for x, y in positions:
			for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
				if 0 <= xx < width and 0 <= yy < height and map[yy][xx] != "#":
					new_positions.add((xx, yy))

		positions = new_positions

	print(len(positions))

if __name__ == "__main__":
	main()