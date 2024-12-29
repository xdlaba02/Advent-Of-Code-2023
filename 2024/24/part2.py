import sys
import re

def main():
	input = sys.stdin.read().strip().split("\n\n")

	regex = re.compile(r"^([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)$")

	operations = [re.match(regex, line).groups() for line in input[1].split("\n")]

	maxZ = max(int(OUT[1:]) for _, _, _, OUT in operations if OUT[0] == "z")

	invalid = []

	for A, OP, B, OUT in operations:
		isXY = (A[0] == "x" and B[0] == "y") or (A[0] == "y" and B[0] == "x")
		is00 = A[1:] == "00" and B[1:] == "00"

		if OUT[0] == "z" and not OP == "XOR" and not int(OUT[1:]) == maxZ:
			invalid.append(OUT)
		elif not OUT[0] == "z" and not isXY and OP == "XOR":
			invalid.append(OUT)
		elif OP == "XOR" and isXY and not is00 and not any(OP2 == "XOR" and (A2 == OUT or B2 == OUT) for A2, OP2, B2, _ in operations):
			invalid.append(OUT)
		elif OP == "AND" and isXY and not is00 and not any(OP2 == "OR" and (A2 == OUT or B2 == OUT) for A2, OP2, B2, _ in operations):
			invalid.append(OUT)

	result = ",".join(sorted(invalid))

	print(result)


if __name__ == "__main__":
	main()