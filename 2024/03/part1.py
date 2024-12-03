import sys
import re

def main():
	input = sys.stdin.read()

	result = sum(int(match.group(1)) * int(match.group(2)) for match in re.finditer(r"mul\((\d+),(\d+)\)", input))

	print(result)

if __name__ == "__main__":
	main()