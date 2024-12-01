import sys

def parse_number(input, index):
	num_str = ""

	while index < len(input) and input[index].isdigit():
		num_str += input[index]
		index += 1

	return (num_str, index)

def is_symbol(c):
	return not c.isdigit() and c != "."

def get_neighbourhood(schematic, line_idx, num_begin, num_end, callback):
	check_line_begin = max(line_idx - 1, 0)
	check_line_end   = min(line_idx + 2, len(schematic))

	check_num_begin = max(num_begin - 1, 0)
	check_num_end   = min(num_end   + 1, len(schematic[line_idx]))

	for y in range(check_line_begin, check_line_end):
		for x in range(check_num_begin, check_num_end):
			callback(x, y)

def main():
	schematic = [row.strip() for row in sys.stdin]

	asterisks = {}

	for line_idx in range(len(schematic)):
		num_begin = 0
		while num_begin < len(schematic[line_idx]):
			num_str, num_end = parse_number(schematic[line_idx], num_begin)

			if num_str:
				def check_neighbourhood(x, y):
					if schematic[y][x] == "*":
						asterisks.setdefault((x, y), []).append(int(num_str))

				get_neighbourhood(schematic, line_idx, num_begin, num_end, check_neighbourhood)

			num_begin = num_end + 1

	sum = 0

	for values in asterisks.values():
		if len(values) == 2:
			sum += values[0] * values[1]

	print(sum)

if __name__ == "__main__":
	main()