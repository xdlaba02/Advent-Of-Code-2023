import sys

def main():
	left, right = zip(*[map(int, row.split()) for row in sys.stdin])

	distance = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

	print(distance)

if __name__ == "__main__":
	main()