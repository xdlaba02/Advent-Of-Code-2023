import sys

def longest_path(graph, start, goal):
	stack = [(start, 0, set())]
	path_len = 0

	while stack:
		node, current_distance, current_path = stack.pop()

		if node == goal:
			path_len = max(path_len, current_distance)
			continue

		for neighbour, distance in graph[node]:
			if neighbour not in current_path:
				stack.append((neighbour, current_distance + distance, current_path | {node}))

	return path_len

def neighbours(map, pos):
	width = len(map[0])
	height = len(map)

	neighbour_list = []

	for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		xx, yy = (pos[0] + dx, pos[1] + dy)

		if 0 <= xx < width and 0 <= yy < height and map[yy][xx] != "#":
			neighbour_list.append((xx, yy))

	return neighbour_list

def main():
	map = [row.strip() for row in sys.stdin]

	width  = len(map[0])
	height = len(map)

	start = (1, 0)
	goal  = (width - 2, height - 1)

	nodes = [start, goal] + [(x, y) for y in range(height) for x in range(width) if len(neighbours(map, (x, y))) > 2 ]

	graph = {}

	for node in nodes:
		for neighbour in neighbours(map, node):
			previous, current = node, neighbour

			distance = 1
			while current not in nodes:
				previous, current = current, [p for p in neighbours(map, current) if p != previous][0]
				distance += 1

			graph.setdefault(node, [])
			graph[node].append((current, distance))

	print(longest_path(graph, start, goal))

if __name__ == "__main__":
	main()