import sys
import collections


def sum_range(a, n):
	return n * a + (n * (n - 1) // 2)


def main():
	line = list(map(int, sys.stdin.read().strip()))

	files = collections.deque(enumerate(line[0::2]))
	spaces = list(reversed(line[1::2]))

	result = 0
	current_length = 0
	
	while files:
		id, length = files.popleft()
		result += id * sum_range(current_length, length)
		current_length += length

		space = spaces.pop()

		while files and space > 0:
			id, length = files[-1]
			if length > space:
				files[-1] = (id, length - space)
				length = space
			elif length <= space:
				files.pop()
			
			result += id * sum_range(current_length, length)
			current_length += length
			space -= length

	print(result)


if __name__ == "__main__":
	main()
