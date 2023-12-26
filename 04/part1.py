import sys

def parse_numbers(numbers_str):
	return set([int(number_str) for number_str in numbers_str.split()])

def main():
	sum = 0

	for line in sys.stdin:
		winning_numbers, numbers = [parse_numbers(numbers_str) for numbers_str in line.split(":")[1].split("|")]

		sum += 2 ** len(winning_numbers & numbers) // 2

	print(sum)

if __name__ == "__main__":
	main()