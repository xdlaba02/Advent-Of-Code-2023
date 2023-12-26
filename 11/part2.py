import sys

def main():
	symbols = [(x, y) for y, line in enumerate(sys.stdin) for x, symbol in enumerate(line) if symbol == "#"]

	width  = max(symbols, key = lambda symbol: symbol[0])[0] + 1
	height = max(symbols, key = lambda symbol: symbol[1])[1] + 1

	column_map = [1000000 - 1] * width
	row_map    = [1000000 - 1] * height

	for symbol in symbols:
		column_map[symbol[0]] = 0
		row_map[symbol[1]]    = 0

	column_map = [sum(column_map[:i + 1]) for i in range(len(column_map))]
	row_map    = [sum(row_map[:i + 1])    for i in range(len(row_map))]

	symbols = [(x + column_map[x], y + row_map[y]) for x, y in symbols]

	result = sum(abs(symbols[i][0] - symbols[j][0]) + abs(symbols[i][1] - symbols[j][1]) for i in range(len(symbols)) for j in range(i + 1, len(symbols)))

	print(result)

if __name__ == "__main__":
	main()