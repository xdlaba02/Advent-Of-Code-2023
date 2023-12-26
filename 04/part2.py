import sys

def parse_numbers(numbers_str):
	return set([int(number_str) for number_str in numbers_str.split()])

def main():
	sum = 0

	win_queue = []

	for line in sys.stdin:
		winning_numbers, numbers = [parse_numbers(numbers_str) for numbers_str in line.split(":")[1].split("|")]

		wins = len(winning_numbers & numbers)

		num_current_cards = 1

		if win_queue:
			num_current_cards += win_queue.pop(0)

		sum += num_current_cards

		for i in range(wins):
			if i < len(win_queue):
				win_queue[i] += num_current_cards
			else:
				win_queue.append(num_current_cards)

	print(sum)

if __name__ == "__main__":
	main()