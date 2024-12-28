import sys
import functools


@functools.cache
def num_possibilities(towels, pattern):
	if not pattern:
		return 1
	
	return sum(num_possibilities(towels, pattern[len(towel):]) for towel in towels if pattern.startswith(towel))


def main():
	input = sys.stdin.read().strip().split("\n\n")

	towels = input[0].split(", ")

	patterns = input[1].split("\n")

	result = sum(num_possibilities(tuple(towels), pattern) for pattern in patterns)

	print(result)


if __name__ == "__main__":
	main()