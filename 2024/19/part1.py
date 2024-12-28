import sys
import functools


@functools.cache
def is_possible(towels, pattern):
	if not pattern:
		return True

	for towel in towels:
		if pattern.startswith(towel) and is_possible(towels, pattern[len(towel):]):
			return True
		
	return False


def main():
	input = sys.stdin.read().strip().split("\n\n")

	towels = input[0].split(", ")

	patterns = input[1].split("\n")

	result = sum(is_possible(tuple(towels), pattern) for pattern in patterns)

	print(result)


if __name__ == "__main__":
	main()