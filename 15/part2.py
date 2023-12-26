import sys
import re

def hash(string):
	hash = 0
	for c in string:
		hash += ord(c)
		hash *= 17
		hash = hash % 256
	return hash

def main():
	strings = sys.stdin.readline().strip().split(",")

	eq_regex   = re.compile(r"^(?P<label>[a-z]+)=(?P<focal_length>\d+)$")
	dash_regex = re.compile(r"^(?P<label>[a-z]+)-$")

	boxes = [[] for _ in range(256)]

	for string in strings:
		if match := eq_regex.match(string):
			label        = match.group("label")
			focal_length = match.group("focal_length")

			index = hash(label)

			for i, box in enumerate(boxes[index]):
				if box[0] == label:
					boxes[index][i] = (label, focal_length)
					break
			else:
				boxes[index].append((label, focal_length))

		if match := dash_regex.match(string):
			label = match.group("label")

			index = hash(label)

			boxes[index] = [(box_label, box_focal_length) for box_label, box_focal_length in boxes[index] if box_label != label]

	sum = 0

	for i, box in enumerate(boxes):
		for j, slot in enumerate(box):
			label, focal_length = slot

			sum += (i + 1) * (j + 1) * int(focal_length)

	print(sum)

if __name__ == "__main__":
	main()