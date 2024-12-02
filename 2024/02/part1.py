import sys

def sign(a):
	return (a > 0) - (a < 0)

def main():
	reports = [list(map(int, row.split())) for row in sys.stdin]

	num_safe = 0

	for report in reports:
		differences = [b - a for a, b in zip(report[:-1], report[1:])]

		if all(sign(difference) == sign(differences[0]) and abs(difference) <= 3 for difference in differences):
			num_safe += 1

	print(num_safe)

if __name__ == "__main__":
	main()