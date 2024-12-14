import sys

def main():
	input = [tuple(map(lambda x: tuple(map(int, x.split("=")[1].split(","))), line.strip().split(" "))) for line in sys.stdin]

	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0

	for p, v in input:
		x = (p[0] + v[0] * 100) % 101
		y = (p[1] + v[1] * 100) % 103
		
		if x < 50:
			if y < 51:
				q1 += 1
			if y > 51:
				q2 += 1
		elif x > 50:
			if y < 51:
				q3 += 1
			if y > 51:
				q4 += 1

	result = q1 * q2 * q3 * q4

	print(result)

if __name__ == "__main__":
	main()