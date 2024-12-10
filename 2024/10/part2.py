import sys


def num_trails(map, pos, level):
	if pos[0] < 0 or pos[0] >= len(map[0]) or pos[1] < 0 or pos[1] >= len(map):
		return 0
	
	if map[pos[1]][pos[0]] != level:
		return 0
	
	if level == 9:
		return 1
	
	return num_trails(map, (pos[0] + 1, pos[1]), level + 1) \
	     + num_trails(map, (pos[0] - 1, pos[1]), level + 1) \
	     + num_trails(map, (pos[0], pos[1] + 1), level + 1) \
	     + num_trails(map, (pos[0], pos[1] - 1), level + 1)
	
def main():
	input = [list(map(int, line.strip())) for line in sys.stdin]

	result = sum(num_trails(input, (x, y), 0) for y in range(len(input)) for x in range(len(input[y])))

	print(result)

if __name__ == "__main__":
	main()
