import sys

def paths(pad, posA, posB):
	if posA == posB:
		return ["A"]
	
	result = []
	
	dX = posB[0] - posA[0]
	dY = posB[1] - posA[1]

	if dX > 0 and (posA[0] + 1, posA[1]) in pad:
		for path in paths(pad, (posA[0] + 1, posA[1]), posB):
			result.append(">" + path)

	if dX < 0 and (posA[0] - 1, posA[1]) in pad:
		for path in paths(pad, (posA[0] - 1, posA[1]), posB):
			result.append("<" + path)

	if dY > 0 and (posA[0], posA[1] + 1) in pad:
		for path in paths(pad, (posA[0], posA[1] + 1), posB):
			result.append("V" + path)

	if dY < 0 and (posA[0], posA[1] - 1) in pad:
		for path in paths(pad, (posA[0], posA[1] - 1), posB):
			result.append("^" + path)

	return result

def shortest_keypad_len(key, depth):
	if depth == 0:
		return len(key)
	
	keypad = {
		"^": (1, 0),
		"A": (2, 0),
		"<": (0, 1),
		"V": (1, 1),
		">": (2, 1),
	}
	
	pos = keypad["A"]

	length = 0

	for symbol in key:
		length += min(shortest_keypad_len(path, depth - 1) for path in paths(keypad.values(), pos, keypad[symbol]))
		pos = keypad[symbol]
	
	return length

def shortest_numpad_len(key):
	numpad = {
		"7": (0, 0),
		"8": (1, 0),
		"9": (2, 0),
		"4": (0, 1),
		"5": (1, 1),
		"6": (2, 1),
		"1": (0, 2),
		"2": (1, 2),
		"3": (2, 2),
		"0": (1, 3),
		"A": (2, 3),
	}
	
	pos = numpad["A"]

	length = 0

	for symbol in key:
		length += min(shortest_keypad_len(path, 2) for path in paths(numpad.values(), pos, numpad[symbol]))
		pos = numpad[symbol]
	
	return length

def main():
	keys = [line.strip() for line in sys.stdin]

	result = sum(shortest_numpad_len(key) * int(key[:3]) for key in keys)

	print(result)


if __name__ == "__main__":
	main()