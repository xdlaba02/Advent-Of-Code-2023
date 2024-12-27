import sys


def main():
	input = sys.stdin.read().strip().split("\n\n")

	registers = [int(register.split(": ")[1]) for register in input[0].split("\n")]

	program = [int(instruction) for instruction in input[1].split(": ")[1].split(",")]

	result = []

	IP = 0
	while IP + 1 < len(program):
		instruction = program[IP]
		operand     = program[IP + 1]

		def combo():
			return operand if operand < 4 else registers[operand - 4]

		if instruction == 0:
			registers[0] >>= combo()
		elif instruction == 1:
			registers[1] ^= operand
		elif instruction == 2:
			registers[1] = combo() % 8
		elif instruction == 3:
			IP = operand - 2 if registers[0] != 0 else IP
		elif instruction == 4:
			registers[1] ^= registers[2]
		elif instruction == 5:
			result.append(str(combo() % 8))
		elif instruction == 6:
			registers[1] = registers[0] >> combo()
		elif instruction == 7:
			registers[2] = registers[0] >> combo()

		IP += 2

	print(",".join(result))


if __name__ == "__main__":
	main()