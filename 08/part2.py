import re
import sys
import math

def main():
	instructions = sys.stdin.readline().strip()

	sys.stdin.readline()

	map_regex = re.compile(r"^(?P<src>...) = \((?P<left>...), (?P<right>...)\)$")

	map = {}

	for line in sys.stdin:
		match = map_regex.match(line)
		map.setdefault(match.group("src"), (match.group("left"), match.group("right")))

	positions = list(filter(lambda position: position[-1] == "A", map.keys()))

	def count_steps(position):
		steps = 0
		while position[-1] != "Z":
			position = map[position][0] if instructions[steps % len(instructions)] == "L" else map[position][1]
			steps += 1
		return steps

	steps = [count_steps(position) for position in positions]
	
	print(math.lcm(*steps))

if __name__ == "__main__":
	main()