import sys

def main():
	schemas = [schema.split("\n") for schema in sys.stdin.read().strip().split("\n\n")]

	keys = []
	locks = []

	for schema in schemas:
		profile = [sum(schema[y][x] == schema[0][0] for y in range(len(schema))) for x in range(len(schema[0]))]
		
		if schema[0][0] == ".":
			keys.append(profile)
		else:
			locks.append(profile)

	result = sum(all(keyDepth >= lockHeight for keyDepth, lockHeight in zip(key, lock)) for lock in locks for key in keys)

	print(result)

if __name__ == "__main__":
	main()