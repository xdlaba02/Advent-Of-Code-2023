import sys
import re

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

def minimal_bag(game):
	return {
		"red":   max([pull["red"]   for pull in game]),
		"green": max([pull["green"] for pull in game]),
		"blue":  max([pull["blue"]  for pull in game]),
	}

def main():

	line_regex = re.compile(r"^Game (?P<game_id>\d+): (?P<game_str>.*)$")

	sum = 0

	for line in sys.stdin:
		if match := line_regex.match(line):
			bag = minimal_bag(parse_game(match.group("game_str")))
			sum += bag["red"] * bag["green"]* bag["blue"]

	print(sum)

if __name__ == "__main__":
	main()