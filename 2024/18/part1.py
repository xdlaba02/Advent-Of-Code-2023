import sys
import heapq

def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])

def inside(pos):
	return 0 <= pos[0] and pos[0] <= 70 and 0 <= pos[1] and pos[1] <= 70

def main():
	bytes = set([tuple(int(val) for val in line.strip().split(",")) for line in sys.stdin][:1024])

	start = (0, 0)
	end = (70, 70)

	positions = []
	costs = {}

	heapq.heappush(positions, (0, start))

	while positions:
		cost, pos = heapq.heappop(positions)

		if pos in bytes or not inside(pos) or cost >= costs.get(pos, float('inf')):
			continue

		costs[pos] = cost

		if pos == end:
			break

		for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
			heapq.heappush(positions, (cost + 1, add_tuples(pos, dir)))
		
	result = costs[end]

	print(result)


if __name__ == "__main__":
	main()