import sys


def iteration(program, A):
	registers = [A, 0, 0]

	for instruction, operand in zip(program[::2], program[1::2]):
		def combo():
			return operand if operand < 4 else registers[operand - 4]
		
		if instruction == 0:
			registers[0] >>= combo()
		elif instruction == 1:
			registers[1] ^= operand
		elif instruction == 2:
			registers[1] = combo() % 8
		elif instruction == 4:
			registers[1] ^= registers[2]
		elif instruction == 5:
			return combo() % 8
		elif instruction == 6:
			registers[1] = registers[0] >> combo()
		elif instruction == 7:
			registers[2] = registers[0] >> combo()


def search(program, A, result):
	if not result:
		return A
	
	for i in range(8):
		if iteration(program, (A << 3) + i) == result[0]:
			if res := search(program, (A << 3) + i, result[1:]):
				return res


def main():
	input = sys.stdin.read().strip().split("\n\n")

	program = [int(instruction) for instruction in input[1].split(": ")[1].split(",")]

	result = search(program, 0, list(reversed(program)))

	print(result)


if __name__ == "__main__":
	main()
