import sys

def extrapolate(list):
	if all([elem == 0 for elem in list]):
		return 0
	
	return list[-1] + extrapolate([list[i + 1] - list[i] for i in range(len(list) - 1)])

def main():
	histories = [[int(reading) for reading in line.split()] for line in sys.stdin]

	print(sum([extrapolate(history) for history in histories]))

if __name__ == "__main__":
	main()