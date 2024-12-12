import sys
import functools

def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])

def measure_region(garden, type, pos):
	if pos[0] < 0 or pos[0] >= len(garden[0]) or pos[1] < 0 or pos[1] >= len(garden):
		return (0, 1)
	
	if garden[pos[1]][pos[0]] == type.lower():
		return (0, 0)

	if garden[pos[1]][pos[0]] != type:
		return (0, 1)
	
	garden[pos[1]][pos[0]] = type.lower()

	return functools.reduce(add_tuples, [
		measure_region(garden, type, add_tuples(pos, (1, 0))),
		measure_region(garden, type, add_tuples(pos, (-1, 0))),
		measure_region(garden, type, add_tuples(pos, (0, 1))),
		measure_region(garden, type, add_tuples(pos, (0, -1))),
		(1, 0)])
	
def main():
	garden = [list(line.strip()) for line in sys.stdin]

	result = 0

	for y in range(len(garden)):
		for x in range(len(garden[y])):
			if not garden[y][x].islower():
				area, perimeter = measure_region(garden, garden[y][x], (x, y))
				result += area * perimeter

	print(result)

if __name__ == "__main__":
	main()