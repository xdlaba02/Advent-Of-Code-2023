import sys

def parse_number(input, index):
	num_str = ""

	while index < len(input) and input[index].isdigit():
		num_str += input[index]
		index += 1

	return (num_str, index)

def is_symbol(c):
	return not c.isdigit() and c != "."

def get_neighbourhood(schematic, line_idx, num_begin, num_end):
	check_line_begin = max(line_idx - 1, 0)
	check_line_end   = min(line_idx + 2, len(schematic))

	check_num_begin = max(num_begin - 1, 0)
	check_num_end   = min(num_end   + 1, len(schematic[line_idx]))

	symbols = ""

	for y in range(check_line_begin, check_line_end):
		for x in range(check_num_begin, check_num_end):
			symbols += schematic[y][x]

	return symbols

def check_neighbourhood(neighbourhood):
	return any([is_symbol(neighbour) for neighbour in neighbourhood])

def main():
	schematic = [row.strip() for row in sys.stdin]

	sum = 0

	for line_idx in range(len(schematic)):
		num_begin = 0
		while num_begin < len(schematic[line_idx]):
			num_str, num_end = parse_number(schematic[line_idx], num_begin)

			if num_str:
				if check_neighbourhood(get_neighbourhood(schematic, line_idx, num_begin, num_end)):
					sum += int(num_str)

			num_begin = num_end + 1

	print(sum)

if __name__ == "__main__":
	main()