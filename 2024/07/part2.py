import sys

def check_operations(target, numbers, acc):
	if not numbers:
		return acc == target

	if acc > target:
		return False

	current, *rest = numbers
	return (
		check_operations(target, rest, acc + current) or
		check_operations(target, rest, acc * current) or
		check_operations(target, rest, int(f"{acc}{current}"))
	)

def main():
	total = 0

	for line in sys.stdin:
		target_str, numbers_str = line.strip().split(":")
		target = int(target_str)
		numbers = list(map(int, numbers_str.split()))

		if check_operations(target, numbers, 0):
			total += target

	print(total)

if __name__ == "__main__":
	main()
