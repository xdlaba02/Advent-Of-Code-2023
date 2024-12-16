import sys
import heapq

def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])


def find_start(maze):
	for y in range(len(maze)):
		for x in range(len(maze[y])):
			if maze[y][x] == "S":
				return (x, y)


def main():
	maze = [list(line.strip()) for line in sys.stdin]

	reindeers = []

	heapq.heappush(reindeers, (0, find_start(maze), (1, 0)))

	costs = {}

	while reindeers:
		cost, pos, dir = heapq.heappop(reindeers)

		symbol = maze[pos[1]][pos[0]]

		if symbol == "E":
			result = cost
			break

		if symbol == "#":
			continue

		key = (pos, abs(dir[0]))

		if cost >= costs.get(key, float('inf')):
			continue

		costs[key] = cost

		heapq.heappush(reindeers, (cost + 1, add_tuples(pos, dir), dir))

		left = (dir[1], -dir[0])
		heapq.heappush(reindeers, (cost + 1001, add_tuples(pos, left), left))

		right = (-dir[1], dir[0])
		heapq.heappush(reindeers, (cost + 1001, add_tuples(pos, right), right))

	print(result)


if __name__ == "__main__":
	main()