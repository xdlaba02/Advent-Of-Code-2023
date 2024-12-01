import sys

def tilt_line(line):
	new_line = line.copy()

	free_spot = 0
	for i, c in enumerate(line):
		if c == "#":
			free_spot = i + 1
		elif c == "O":
			new_line[i] = '.'
			new_line[free_spot] = 'O'
			free_spot += 1

	return new_line

def tilt_dish(dish):
	return [tilt_line(line) for line in dish]

def score_line(line):
	score = 0

	for i, c in enumerate(line):
		if c == "O":
			score += len(line) - i

	return score

def score_dish(dish):
	return sum([score_line(line) for line in dish])

def transpose(dish):
	return [[row[i] for row in dish] for i in range(len(dish[0]))]

def rotate_left(dish):
	return transpose(dish)[::-1]

def rotate_right(dish):
	return [list(reversed(row)) for row in transpose(dish)]

def cycle_dish(dish):
	for i in range(4):
		dish = rotate_right(tilt_dish(dish))

	return dish

def main():
	dish = [list(row.strip()) for row in sys.stdin]

	dish = rotate_left(dish)

	history = []

	while dish not in history:
		history.append(dish)
		dish = cycle_dish(dish)

	cycle_init = history.index(dish)
	cycle_len = len(history) - cycle_init

	print(score_dish(history[cycle_init + ((1_000_000_000 - cycle_init) % cycle_len)]))

if __name__ == "__main__":
	main()