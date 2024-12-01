import sys
import collections

def main():
	left, right = zip(*[map(int, row.split()) for row in sys.stdin])

	left_histogram = collections.Counter(left)
	right_histogram = collections.Counter(right)

	score = sum(key * value * right_histogram[key] for key, value in left_histogram.items() if key in right_histogram)

	print(score)

if __name__ == "__main__":
	main()