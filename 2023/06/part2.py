import sys
import math

def main():
	time     = int(sys.stdin.readline().split(":")[1].replace(" ", ""))
	distance = int(sys.stdin.readline().split(":")[1].replace(" ", ""))

	root_range = math.sqrt(time ** 2 - 4 * distance)

	print(round(root_range))

if __name__ == "__main__":
	main()