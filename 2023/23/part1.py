import sys

def longest_path(map, start, goal):
	width = len(map[0])
	height = len(map)

	stack = [(start, set())]
	path_len = 0

	def step_valid(node, direction):
		return (node == "." or 
		        node == ">" and direction != (-1,  0) or 
		        node == "<" and direction != ( 1,  0) or
		        node == "^" and direction != ( 0,  1) or
		        node == "v" and direction != ( 0, -1)
		)

	while stack:
		(x, y), current_path = stack.pop()

		if (x, y) == goal:
			path_len = max(path_len, len(current_path))
			continue

		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			xx, yy = (x + dx, y + dy)

			if 0 <= xx < width and 0 <= yy < height and (xx, yy) not in current_path and step_valid(map[yy][xx], (dx, dy)):
				stack.append(((xx, yy), current_path | {(x, y)}))

	return path_len

def main():
	map = [row.strip() for row in sys.stdin]

	width  = len(map[0])
	height = len(map)

	start = (1, 0)
	goal  = (width - 2, height - 1)

	print(longest_path(map, start, goal))

if __name__ == "__main__":
	main()