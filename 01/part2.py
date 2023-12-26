import sys

def parse_digit(string):
	if string.startswith("zero"):
		return 0
	if string.startswith("one"):
		return 1
	if string.startswith("two"):
		return 2
	if string.startswith("three"):
		return 3
	if string.startswith("four"):
		return 4
	if string.startswith("five"):
		return 5
	if string.startswith("six"):
		return 6
	if string.startswith("seven"):
		return 7
	if string.startswith("eight"):
		return 8
	if string.startswith("nine"):
		return 9
	if string[0].isdigit():
		return int(string[0])
	
	return None
	
def main():
	sum = 0

	for line in sys.stdin:
		num = 0

		len_range = range(len(line))

		for i in len_range:
			digit = parse_digit(line[i:])
			if digit:
				num += digit * 10
				break

		for i in reversed(len_range):
			digit = parse_digit(line[i:])
			if digit:
				num += digit
				break

		sum += num

	print(sum)

if __name__ == "__main__":
	main()