import sys

def defects(lines, index):
	return sum(sum(a != b for a, b in zip(line_a, line_b)) for line_a, line_b in zip(reversed(lines[:index]), lines[index:]))

def transpose(matrix):
	return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def find_mirrorline(pattern, num_defects):
	for i in range(1, len(pattern)):
		if defects(pattern, i) == num_defects:
			return i
		
	return 0

def summarize(pattern):
	return find_mirrorline(pattern, 1) * 100 + find_mirrorline(transpose(pattern), 1)

def main():
	patterns = [list(filter(None, group.split("\n"))) for group in sys.stdin.read().split("\n\n")]

	result = sum([summarize(pattern) for pattern in patterns])

	print(result)

if __name__ == "__main__":
	main()