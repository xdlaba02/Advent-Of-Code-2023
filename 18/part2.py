import sys
import re

def main():

	line_regex = re.compile(r"^(U|D|L|R) \d+ \(#(?P<distance>[a-f0-9]{5})(?P<direction>(0|1|2|3))\)$")

	area = 0

	x, y = 0, 0
	for line in sys.stdin:
		match = line_regex.match(line.strip())

		direction = match.group("direction")
		distance  = int(match.group("distance"), 16)

		dx, dy = {
			"0": ( 1,  0),
			"1": ( 0,  1),
			"2": (-1,  0),
			"3": ( 0, -1),
		}[direction]

		new_x = x + distance * dx
		new_y = y + distance * dy

		# Add perimeter to the area
		area += distance

		area += (y + new_y) * (x - new_x)

		x = new_x
		y = new_y

	print(area // 2 + 1)

if __name__ == "__main__":
	main()