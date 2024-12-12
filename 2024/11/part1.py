import sys

def split_stone(stone, iterations):
	if iterations == 0:
		return 1
	
	if stone == 0:
		return split_stone(1, iterations - 1)

	stone_str = str(stone)
	stone_str_len = len(stone_str)
	if stone_str_len % 2 == 0:
		return split_stone(int(stone_str[:stone_str_len // 2]), iterations - 1) + split_stone(int(stone_str[stone_str_len // 2:]), iterations - 1)

	return split_stone(stone * 2024, iterations - 1)
	
def main():
	stones = map(int, sys.stdin.read().split())

	result = sum(split_stone(stone, 25) for stone in stones)

	print(result)

if __name__ == "__main__":
	main()