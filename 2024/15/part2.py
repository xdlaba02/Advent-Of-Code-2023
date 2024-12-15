import sys

def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])

def find_robot(warehouse):
	for y in range(len(warehouse)):
		for x in range(len(warehouse[y])):
			if warehouse[y][x] == "@":
				return (x, y)
			
def direction(step):
	if step == ">":
		return (1, 0)
	elif step == "v":
		return (0, 1)
	elif step == "<":
		return (-1, 0)
	elif step == "^":
		return (0, -1)
	
def move(warehouse, positions, dir):
	positions = set(pos for pos in positions if warehouse[pos[1]][pos[0]] != ".")

	if not positions:
		return True
	
	if "#" in (warehouse[pos[1]][pos[0]] for pos in positions):
		return False

	if dir in [(0, 1), (0, -1)]:
		complete_positions = set()

		for pos in positions:
			complete_positions.add(pos)

			symbol = warehouse[pos[1]][pos[0]]
			if symbol == "[":
				complete_positions.add((pos[0] + 1, pos[1]))
			if symbol == "]":
				complete_positions.add((pos[0] - 1, pos[1]))

		positions = complete_positions

	if move(warehouse, set(add_tuples(pos, dir) for pos in positions), dir):
		for pos in positions:
			next_pos = add_tuples(pos, dir)
			warehouse[next_pos[1]][next_pos[0]] = warehouse[pos[1]][pos[0]]
			warehouse[pos[1]][pos[0]] = "."
		return True
	else:
		return False
	
def widen(line):
	result = []
	for c in line:
		if c == "#":
			result += ["#", "#"]
		elif c == "O":
			result += ["[", "]"]
		elif c == ".":
			result += [".", "."]
		elif c == "@":
			result += ["@", "."]
	return result

def main():
	data = sys.stdin.read().strip().split("\n\n")

	warehouse = [widen(line) for line in data[0].split("\n")]

	steps = list(data[1].replace("\n", ""))

	robot = find_robot(warehouse)

	for step in steps:
		dir = direction(step)
		if move(warehouse, set([robot]), dir):
			robot = add_tuples(robot, dir)

	result = sum(y * 100 + x for y in range(len(warehouse)) for x in range(len(warehouse[y])) if warehouse[y][x] == "[")

	print(result)


if __name__ == "__main__":
	main()