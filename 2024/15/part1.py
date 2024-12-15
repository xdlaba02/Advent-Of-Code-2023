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
			
def move(warehouse, pos, dir):
	if warehouse[pos[1]][pos[0]] == "#":
		return False
	
	if warehouse[pos[1]][pos[0]] == ".":
		return True
	
	next_pos = add_tuples(pos, dir)
	
	if move(warehouse, next_pos, dir):
		warehouse[next_pos[1]][next_pos[0]] = warehouse[pos[1]][pos[0]]
		warehouse[pos[1]][pos[0]] = "."
		return True
	else:
		return False
	

def main():
	input = sys.stdin.read().strip().split("\n\n")

	warehouse = [list(line) for line in input[0].split("\n")]
	steps = list(input[1].replace("\n", ""))

	robot = find_robot(warehouse)

	for step in steps:
		dir = direction(step)
		if move(warehouse, robot, dir):
			robot = add_tuples(robot, dir)

	result = sum(y * 100 + x for y in range(len(warehouse)) for x in range(len(warehouse[y])) if warehouse[y][x] == "O")

	print(result)


if __name__ == "__main__":
	main()