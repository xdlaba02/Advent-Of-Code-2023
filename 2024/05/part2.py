import sys
import functools

def check_update(rules, update):
	for i, value in enumerate(update):
		for j in range(i):
			if update[j] in rules.get(value, []):
				return False
	return True

def evaluate_update(rules, elements):
	def compare(x, y):
		return -1 if y in rules.get(x, []) else 1 if x in rules.get(y, []) else 0

	return int(sorted(elements, key = functools.cmp_to_key(compare))[len(elements) // 2]) if not check_update(rules, elements) else 0

def main():
	rules = {}

	for line in sys.stdin:
		line = line.strip()

		if not line:
			break
		
		key, value = line.split("|")

		rules.setdefault(key, []).append(value)

	result = sum(evaluate_update(rules, line.strip().split(",")) for line in sys.stdin)

	print(result)

if __name__ == "__main__":
	main()