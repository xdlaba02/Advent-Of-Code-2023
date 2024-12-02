import sys

def sign(a):
	return (a > 0) - (a < 0)

def safe(report):
	differences = [b - a for a, b in zip(report[:-1], report[1:])]
	return all(difference != 0 and abs(difference) <= 3 and sign(difference) == sign(differences[0]) for difference in differences)

def main():
	reports = [list(map(int, row.split())) for row in sys.stdin]

	num_safe = sum(any(safe(report[:i] + report[i + 1:]) for i in range(len(report))) for report in reports)

	print(num_safe)

if __name__ == "__main__":
	main()