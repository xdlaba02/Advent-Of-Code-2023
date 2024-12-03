import sys
import re

def main():
	input = sys.stdin.read()

	filtered_input = re.sub(r"don't\(\)[\s\S]*?(do\(\)|$)", "|", input)

	result = sum(int(match.group(1)) * int(match.group(2)) for match in re.finditer(r"mul\((\d+),(\d+)\)", filtered_input))

	print(result)

if __name__ == "__main__":
	main()