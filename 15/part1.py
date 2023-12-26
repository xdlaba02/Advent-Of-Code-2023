import sys

def main():
	strings = sys.stdin.readline().strip().split(",")

	sum = 0

	for string in strings:
		hash = 0
		for c in string:
			hash += ord(c)
			hash *= 17
			hash = hash % 256
		sum += hash

	print(sum)

if __name__ == "__main__":
	main()