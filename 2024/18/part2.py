import sys


def add_tuples(a, b):
	return (a[0] + b[0], a[1] + b[1])


def inside(pos):
	return 0 <= pos[0] and pos[0] <= 70 and 0 <= pos[1] and pos[1] <= 70


def path_exists(bytes):
	start = (0, 0)
	end = (70, 70)

	positions = [start]
	costs = {}

	while positions:
		pos = positions.pop()

		if pos == end:
			return True

		if pos in bytes or not inside(pos):
			continue
		
		cost = abs(end[0] - pos[0]) + abs(end[1] - pos[1])

		if cost >= costs.get(pos, float('inf')):
			continue

		costs[pos] = cost

		for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			positions.append(add_tuples(pos, dir))
		
	return False


def binary_search(bytes, begin, end, result):
	if begin >= end:
		return result
	
	pivot = (begin + end) // 2

	if path_exists(bytes[:pivot + 1]):
		return binary_search(bytes, pivot + 1, end, result)
	else:
		return binary_search(bytes, begin, pivot, bytes[pivot])


def main():
	bytes = [tuple(int(val) for val in line.strip().split(",")) for line in sys.stdin]

	result = binary_search(bytes, 0, len(bytes), None)

	print(f"{result[0]},{result[1]}")


if __name__ == "__main__":
	main()