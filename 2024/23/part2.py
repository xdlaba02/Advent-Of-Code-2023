import sys


def get_largest_clique(network):
	largest_clique = []

	keys = list(network)
	for i, node in enumerate(keys):
		new_clique = get_largest_clique({ key: network[key] for key in keys[i + 1:] if key in network[node] })
		
		if len(new_clique) + 1 > len(largest_clique):
			largest_clique = new_clique + [node]
		
	return largest_clique


def main():
	network = {}

	input = [line.strip().split("-") for line in sys.stdin]

	for A, B in input:
		network.setdefault(A, [])
		network.setdefault(B, [])
		network[A].append(B)
		network[B].append(A)

	result = sorted(get_largest_clique(network))

	print(",".join(result))


if __name__ == "__main__":
	main()