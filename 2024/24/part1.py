import sys
import re


def main():
	input = sys.stdin.read().strip().split("\n\n")

	variables = {}

	for line in input[0].split("\n"):
		variable, value = line.split(": ")
		variables[variable] = int(value)

	operations = {}

	regex = re.compile(r"^([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)$")
	
	for line in input[1].split("\n"):
		match = re.match(regex, line)
		operations[match.group(4)] = (match.group(2), match.group(1), match.group(3))

	def value(variable):
		if variable in variables:
			return variables[variable]
		
		OP, A, B = operations[variable]

		if OP == "AND":
			variables[variable] = value(A) & value(B)
		elif OP == "OR":
			variables[variable] = value(A) | value(B)
		elif OP == "XOR":
			variables[variable] = value(A) ^ value(B)

		return value(variable)
	
	result = 0
	
	for i, variable in enumerate(sorted(variable for variable in operations if variable[0] == "z")):
		result |= value(variable) << i

	print(result)


if __name__ == "__main__":
	main()