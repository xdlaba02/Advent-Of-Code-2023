import sys
import re

def color_possible(bag_count, pull_count):
	return bag_count >= pull_count

def pull_possible(bag_counts, pull_counts):
	return all([color_possible(bag_counts[color], count) for color, count in pull_counts.items()])

def game_possible(bag_counts, pulls):
	return all([pull_possible(bag_counts, pull) for pull in pulls])

def parse_pull(pull_str):
	pull = {
		"red":   0,
		"green": 0,
		"blue":  0,
	}

	for color_pull in pull_str.split(","):
		color_pull_elems = color_pull.split()

		pull_count = int(color_pull_elems[0])
		pull_color = color_pull_elems[1]

		pull[pull_color] = pull_count

	return pull

def parse_game(game_str):
	return [parse_pull(pull_str) for pull_str in game_str.split(";")]

def main():

	line_regex = re.compile(r"^Game (?P<game_id>\d+): (?P<game_str>.*)$")

	sum = 0

	for line in sys.stdin:
		if match := line_regex.match(line):
			if game_possible({"red": 12, "green": 13, "blue": 14}, parse_game(match.group("game_str"))):
				sum += int(match.group("game_id"))

	print(sum)

if __name__ == "__main__":
	main()