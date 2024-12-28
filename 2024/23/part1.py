import sys


def main():
	network = {}

	input = [line.strip().split("-") for line in sys.stdin]

	for A, B in input:
		network.setdefault(min(A, B), [])
		network[min(A, B)].append(max(A, B))

	for key in network:
		network[key].sort()

	result = 0

	for computerA, connectionsA in network.items():
		for i in range(len(connectionsA)):
			computerB = connectionsA[i]
			for j in range(i + 1, len(connectionsA)):
				computerC = connectionsA[j]
				result += computerC in network.get(computerB, []) and (computerA[0] == "t" or computerB[0] == "t" or computerC[0] == "t")

	print(result)


if __name__ == "__main__":
	main()