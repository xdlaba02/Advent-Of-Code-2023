import sys

def follow(contraption, visit_map, position, direction):
	while True:
		x, y   = position

		if 0 > x or x >= len(contraption[0]):
			return
		
		if 0 > y or y >= len(contraption):
			return
		
		visit_map_idx = {
			( 1,  0): 0,
			(-1,  0): 1,
			( 0,  1): 2,
			( 0, -1): 3,
		}[direction]

		if visit_map[y][x][visit_map_idx]:
			return

		visit_map[y][x][visit_map_idx] = True

		symbol = contraption[y][x]

		if symbol == "\\":
			direction = (direction[1], direction[0])

		elif symbol == "/":
			direction = (-direction[1], -direction[0])

		elif symbol == "-" and direction[1]:
			follow(contraption, visit_map, (x + 1, y), (1, 0))
			direction = (-1, 0)

		elif symbol == "|" and direction[0]:
			follow(contraption, visit_map, (x, y + 1), (0, 1))
			direction = (0, -1)
		
		position = (x + direction[0], y + direction[1])


def main():
	contraption = [list(row.strip()) for row in sys.stdin]

	visit_map = [[[False, False, False, False] for _ in line] for line in contraption]

	follow(contraption, visit_map, (0, 0), (1, 0))

	visited_positions = sum([sum([any(element) for element in line]) for line in visit_map])

	print(visited_positions)

if __name__ == "__main__":
	main()