import sys

def main():
	input = sys.stdin.read().strip().split("\n\n")

	registers = [register.split(": ")[1] for register in input[0].split("\n")]

	program = [int(instruction) for instruction in input[1].split(": ")[1].split(",")]

	IP = 0
	while IP + 1 < len(program):
		instruction = program[IP]
		operand     = program[IP + 1]

		operand_value = operand if operand < 4 else registers[operand - 4]

if __name__ == "__main__":
	main()