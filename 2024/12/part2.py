import sys

def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])

def visit_region(garden, type, pos, visitor):
	if pos[0] < 0 or pos[0] >= len(garden[0]) or pos[1] < 0 or pos[1] >= len(garden):
		return
	
	if garden[pos[1]][pos[0]] != type:
		return
	
	garden[pos[1]][pos[0]] = "."

	visit_region(garden, type, add_tuples(pos, (1, 0)), visitor)
	visit_region(garden, type, add_tuples(pos, (-1, 0)), visitor)
	visit_region(garden, type, add_tuples(pos, (0, 1)), visitor)
	visit_region(garden, type, add_tuples(pos, (0, -1)), visitor)

	visitor(pos)

def count_corners(region):
	corners = 0
	for pos in region:
		for h in [1, -1]:
			if add_tuples(pos, (h, 0)) in region:
				for v in [1, -1]:
					corners += add_tuples(pos, (0, v)) in region and add_tuples(pos, (h, v)) not in region
			else:
				for v in [1, -1]:
					corners += add_tuples(pos, (0, v)) not in region
	return corners
	
def main():
	garden = [list(line.strip()) for line in sys.stdin]

	result = 0

	for y in range(len(garden)):
		for x in range(len(garden[y])):
			if garden[y][x] != ".":
				region = set()
				visit_region(garden, garden[y][x], (x, y), lambda x: region.add(x))
				result += len(region) * count_corners(region)

	print(result)

if __name__ == "__main__":
	main()