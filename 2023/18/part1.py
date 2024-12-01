import sys
import re

def main():
	line_regex = re.compile(r"^(?P<direction>(U|D|L|R)) (?P<distance>\d+) \(#[a-f0-9]{6}\)$")

	area = 0

	x, y = 0, 0
	for line in sys.stdin:
		match = line_regex.match(line.strip())

		direction = match.group("direction")
		distance  = int(match.group("distance"))

		dx, dy = {
			"R": ( 1,  0),
			"L": (-1,  0),
			"D": ( 0,  1),
			"U": ( 0, -1),
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