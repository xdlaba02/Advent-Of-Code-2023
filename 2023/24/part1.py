import sys

def hailstone_cross(a, b):
	(xa, ya), (dxa, dya) = a
	(xb, yb), (dxb, dyb) = b

	determinant = dxa * dyb - dya * dxb

	if determinant == 0:
		return None

	t = ((xb - xa) * dyb - (yb - ya) * dxb) / determinant
	s = ((xb - xa) * dya - (yb - ya) * dxa) / determinant

	return (xa + t * dxa, ya + t * dya) if t >= 0 and s >= 0 else None

def main():
	hailstones = []

	for line in sys.stdin:
		position, velocity = [[int(value) for value in values.split(", ")[:2]] for values in line.split(" @ ")]
		hailstones.append((position, velocity))

	range_min = 200000000000000
	range_max = 400000000000000

	num = 0

	for i in range(len(hailstones)):
		for j in range(i + 1, len(hailstones)):
			if cross := hailstone_cross(hailstones[i], hailstones[j]):
				if all(range_min <= crossing <= range_max for crossing in cross):
					num += 1

	print(num)

if __name__ == "__main__":
	main()