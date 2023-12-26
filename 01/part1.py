import sys

def parse_digit(string):
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