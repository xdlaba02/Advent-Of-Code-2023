import sys

def sum_range(a, n):
	return n * a + (n * (n - 1) // 2)

def main():
	line = list(map(int, sys.stdin.read().strip()))

	files = []
	spaces = []
	position = 0
	for i, length in enumerate(line):
		if i % 2 == 0:
			files.append((position, length))
		else:
			spaces.append((position, length))

		position += length

	for i in range(len(files) - 1, -1, -1):
		file_position, file_length = files[i]
		for j in range(len(spaces)):
			space_position, space_length = spaces[j]

			if space_position < file_position and space_length >= file_length:
				files[i] = (space_position, file_length)
				spaces[j] = (space_position + file_length, space_length - file_length)
				break

	result = sum(i * sum_range(position, length) for i, (position, length) in enumerate(files))

	print(result)

if __name__ == "__main__":
	main()
