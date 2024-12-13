import sys
import re

def solve_equations(A, B, target):
	nA = (target[0] * B[1] - target[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
	nB = (target[0] - A[0] * nA) / B[0]
	return (nA, nB)

def parse_input_line(line):
	match = re.search(r"(\d+).+?(\d+)", line)
	return (int(match.group(1)), int(match.group(2)))

def main():
	input = [[parse_input_line(line) for line in group.split("\n")] for group in sys.stdin.read().strip().split("\n\n")]

	result = 0

	for A, B, target in input:
		nA, nB = solve_equations(A, B, (10000000000000 + target[0], 10000000000000 + target[1]))

		if nA.is_integer() and nB.is_integer():
			result += int(nA * 3 + nB)

	print(result)

if __name__ == "__main__":
	main()