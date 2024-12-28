import sys


def next_number(seed):
	seed = ((seed << 6) ^ seed) & 0xFFFFFF
	seed = ((seed >> 5) ^ seed) & 0xFFFFFF
	seed = ((seed << 11) ^ seed) & 0xFFFFFF
	return seed


def random_sequence(seed):
	while True:
		yield seed
		seed = next_number(seed)


def take(generator, n):
	i = 0
	for value in generator:
		if i < n:
			yield value
			i += 1
		else:
			return


def modulo(generator, n):
	for current in generator:
		yield current % n


def sequence_generator(generator, window_size):
	window = []
	prev = next(generator, None)
	
	if prev is None:
		return
	
	for current in generator:
		window.append(current - prev)
		if len(window) > window_size:
			window.pop(0)
		
		if len(window) == window_size:
			yield tuple(window), current
		
		prev = current


def banana_sequences(seed):
	sequences = {}

	for diffs, value in sequence_generator(take(modulo(random_sequence(seed), 10), 2000), 4):
		if diffs not in sequences:
			sequences[diffs] = value

	return sequences
	
	
def main():
	seeds = [int(line.strip()) for line in sys.stdin]

	sequences = {}

	for seed in seeds:
		for key, value in banana_sequences(seed).items():
			sequences[key] = sequences.get(key, 0) + value

	result = max(sequences.values())

	print(result)


if __name__ == "__main__":
	main()