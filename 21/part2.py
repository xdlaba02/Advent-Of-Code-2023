import sys
import numpy 

def advance(garden, positions):
	side = len(garden)

	new_positions = set()
		
	for x, y in positions:
		for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

			if garden[yy % side][xx % side] != "#":
				new_positions.add((xx, yy))

	return new_positions

def main():
	garden = [row.strip() for row in sys.stdin]

	side = len(garden)

	positions = set()

	for y, row in enumerate(garden):
		for x, c in enumerate(row):
			if c == "S":
				positions.add((x, y))

	for i in range(side // 2):
		positions = advance(garden, positions)

	a = len(positions)

	for i in range(side):
		positions = advance(garden, positions)

	b = len(positions)

	for i in range(side):
		positions = advance(garden, positions)

	c = len(positions)

	coefficients = numpy.polyfit([side // 2, side // 2 + side, side // 2 + side * 2], [a, b, c], deg = 2)
	
	print(int(numpy.polyval(coefficients, 26501365)))

if __name__ == "__main__":
	main()