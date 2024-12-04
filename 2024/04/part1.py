import sys

def check_xmas(input, x, y, dx, dy):
	for c in "XMAS":
		if y < 0 or x < 0 or y >= len(input) or x >= len(input[y]):
			return False

		if input[y][x] != c:
			return False
		
		x += dx
		y += dy

	return True

def main():
	input = [line.strip() for line in sys.stdin]

	output = 0

	for y in range(len(input)):
		for x in range(len(input[y])):
			for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
				output += check_xmas(input, x, y, dx, dy)

	print(output)

if __name__ == "__main__":
	main()