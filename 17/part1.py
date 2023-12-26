import sys
import heapq

def heuristic(pos, goal):
	return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

def orthogonals(direction):
	return [(-direction[1], direction[0]), (direction[1], -direction[0])]

def steps(direction, n):
	return [(direction[0] * (i + 1), direction[1] * (i + 1)) for i in range(n)]

def shortest_path(map, start, goal):
	width = len(map[0])
	height = len(map)

	queue = []
	closed = {}

	heapq.heappush(queue, (heuristic(start, goal), 0, start, (1, 0)))
	heapq.heappush(queue, (heuristic(start, goal), 0, start, (0, 1)))

	while queue:
		_, distance, node, direction = heapq.heappop(queue)

		if node == goal:
			return distance
		
		closed_key = (node, (abs(direction[0]), abs(direction[1])))
					
		if closed_key not in closed or closed[closed_key] > distance:

			closed[closed_key] = distance

			for new_direction in orthogonals(direction):

				for i in range(3):
					path = [(node[0] + step[0], node[1] + step[1]) for step in steps(new_direction, i + 1)]

					destination = path[-1]

					if 0 <= destination[0] < width and 0 <= destination[1] < height:

						new_distance = distance + sum([map[neighbor[1]][neighbor[0]] for neighbor in path])

						new_score = new_distance + heuristic(node, goal)

						heapq.heappush(queue, (new_score, new_distance, destination, new_direction))

def main():
	map = [[int(c) for c in row.strip()] for row in sys.stdin]

	width = len(map[0])
	height = len(map)

	start = (0, 0)
	goal  = (width - 1, height - 1)

	print(shortest_path(map, start, goal))


if __name__ == "__main__":
	main()