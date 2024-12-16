import sys
import heapq
import math

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

	start = find_start(maze)

	heapq.heappush(reindeers, (0, [start], (1, 0)))

	costs = {}
	tiles = set()

	lowest_cost = math.inf

	while reindeers:
		cost, path, dir = heapq.heappop(reindeers)

		pos = path[-1]

		element = maze[pos[1]][pos[0]]

		if cost > lowest_cost:
			break

		if element == "E":
			lowest_cost = cost
			tiles.update(path)
			continue

		if element == "#":
			continue

		key = (pos, abs(dir[0]))

		if key in costs and costs[key] < cost:
			continue

		costs[key] = cost

		heapq.heappush(reindeers, (cost + 1, path + [add_tuples(pos, dir)], dir))

		left = (dir[1], -dir[0])
		heapq.heappush(reindeers, (cost + 1001, path + [add_tuples(pos, left)], left))

		right = (-dir[1], dir[0])
		heapq.heappush(reindeers, (cost + 1001, path + [add_tuples(pos, right)], right))

	print(len(tiles))


if __name__ == "__main__":
	main()