import sys

def check_update(rules, update):
	for i, value in enumerate(update):
		for j in range(i):
			if update[j] in rules.get(value, []):
				return False
	return True

def evaluate_update(rules, update):
	return int(update[len(update) // 2]) if check_update(rules, update) else 0

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