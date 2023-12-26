import sys

def tilt_left_score(line):
	score = 0

	free_spot = 0
	for i, c in enumerate(line):
		if c == "#":
			free_spot = i + 1
		elif c == "O":
			score += len(line) - free_spot
			free_spot += 1

	return score

def transpose(matrix):
	return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def main():
	dish = [list(row.strip()) for row in sys.stdin]

	load = sum([tilt_left_score(line) for line in transpose(dish)])

	print(load)

if __name__ == "__main__":
	main()