import sys
import itertools
import operator

def main():
	symbols = []

	for y, line in enumerate(sys.stdin):
		for x, symbol in enumerate(line):
			if symbol == "#":
				symbols.append((x, y))

	width  = max(symbols, key = lambda symbol: symbol[0])[0] + 1
	height = max(symbols, key = lambda symbol: symbol[1])[1] + 1

	column_map = [1] * width
	row_map    = [1] * height

	for symbol in symbols:
		column_map[symbol[0]] = 0
		row_map[symbol[1]]    = 0

	column_cumsum = list(itertools.accumulate(column_map, operator.add))
	row_cumsum    = list(itertools.accumulate(row_map, operator.add))

	expanded_symbols = [(x + column_cumsum[x], y + row_cumsum[y]) for x, y in symbols]

	sum = 0

	for i in range(len(expanded_symbols)):
		for j in range(i + 1, len(expanded_symbols)):
			sum += abs(expanded_symbols[i][0] - expanded_symbols[j][0]) + abs(expanded_symbols[i][1] - expanded_symbols[j][1])

	print(sum)

if __name__ == "__main__":
	main()