import sys
import sympy

def main():
	hailstones = []

	for line in sys.stdin:
		position, velocity = [[int(value) for value in values.split(", ")] for values in line.split(" @ ")]
		hailstones.append((position, velocity))

	x, y, z, dx, dy, dz, t, u, v = sympy.symbols("x y z dx dy dz t u v")

	equations = [sympy.Eq(hailstones[i][0][j] + hailstones[i][1][j] * param, pos + dir * param) for i, param in enumerate([t, u, v]) for j, (pos, dir) in enumerate([(x, dx), (y, dy), (z, dz)])]

	solution = sympy.solve(equations, (x, y, z, dx, dy, dz, t, u, v))[0]

	print(solution[0] + solution[1] + solution[2])

if __name__ == "__main__":
	main()