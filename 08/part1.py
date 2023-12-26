import re
import sys

def main():
	instructions = sys.stdin.readline().strip()

	sys.stdin.readline()

	map_regex = re.compile(r"^(?P<src>...) = \((?P<left>...), (?P<right>...)\)$")

	map = {}

	for line in sys.stdin:
		match = map_regex.match(line)
		map.setdefault(match.group("src"), (match.group("left"), match.group("right")))

	position = "AAA"

	steps = 0
	while position != "ZZZ":
		position = map[position][0] if instructions[steps % len(instructions)] == "L" else map[position][1]
		steps += 1

	print(steps)

if __name__ == "__main__":
	main()