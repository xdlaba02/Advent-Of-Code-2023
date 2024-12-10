import sys


def trails(map, pos, level):
	if pos[0] < 0 or pos[0] >= len(map[0]) or pos[1] < 0 or pos[1] >= len(map):
		return []
	
	if map[pos[1]][pos[0]] != level:
		return []
	
	if level == 9:
		return [pos]
	
	return trails(map, (pos[0] + 1, pos[1]), level + 1) \
	     + trails(map, (pos[0] - 1, pos[1]), level + 1) \
	     + trails(map, (pos[0], pos[1] + 1), level + 1) \
	     + trails(map, (pos[0], pos[1] - 1), level + 1)
	
def main():
	input = [list(map(int, line.strip())) for line in sys.stdin]

	result = sum(len(set(trails(input, (x, y), 0))) for y in range(len(input)) for x in range(len(input[y])))

	print(result)

if __name__ == "__main__":
	main()
