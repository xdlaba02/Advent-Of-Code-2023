import sys

def check_mas(input, x, y, dx, dy):
	for c in "MAS":
		if input[y][x] != c:
			return False
		
		x += dx
		y += dy

	return True

def check_xmas(input, x, y):
	return any(check_mas(input, x - dx, y - dy, dx, dy) for dx, dy in [(1, 1), (-1, -1)]) and any(check_mas(input, x - dx, y - dy, dx, dy) for dx, dy in [(-1, 1), (1, -1)])

def main():
	input = [line.strip() for line in sys.stdin]

	output = sum(check_xmas(input, x, y) for y in range(1, len(input) - 1) for x in range(1, len(input[y]) - 1))

	print(output)

if __name__ == "__main__":
	main()