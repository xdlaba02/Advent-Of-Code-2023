import sys


def nth_number(seed, iterations):
	for _ in range(iterations):
		seed = next_number(seed)
	return seed


def next_number(seed):
	seed = ((seed << 6) ^ seed) & 0xFFFFFF
	seed = ((seed >> 5) ^ seed) & 0xFFFFFF
	seed = ((seed << 11) ^ seed) & 0xFFFFFF
	return seed


def main():
	seeds = [int(line.strip()) for line in sys.stdin]

	result = sum(nth_number(seed, 2000) for seed in seeds)

	print(result)


if __name__ == "__main__":
	main()