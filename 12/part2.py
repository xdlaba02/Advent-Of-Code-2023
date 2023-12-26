import sys
import functools 

def operational(c):
	return c in "?."

def damaged(c):
	return c in "?#"

def valid_sequence(sublist, length):
	if len(sublist) < length:
		return False
	
	if len(sublist) > length:
		if not operational(sublist[length]):
			return False
		
	for i in range(length):
		if not damaged(sublist[i]):
			return False
		
	return True

@functools.cache
def possible_arrangements(springs, numbers):
	if not numbers:
		return all(operational(spring) for spring in springs)
	
	if not springs:
		return not numbers

	sum = 0

	if operational(springs[0]):
		sum += possible_arrangements(springs[1:], numbers)
	
	if damaged(springs[0]) and valid_sequence(springs, numbers[0]):
		sum += possible_arrangements(springs[numbers[0] + 1:], numbers[1:])

	return sum

def main():
	arrangements = 0

	for line in sys.stdin:
		springs, numbers_str = line.split()
		numbers = tuple(int(number) for number in numbers_str.split(","))

		arrangements += possible_arrangements("?".join([springs] * 5), numbers * 5)

	print(arrangements)

if __name__ == "__main__":
	main()