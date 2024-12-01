import sys

def brick_blocks_2D(brick):
	(x1, y1, _), (x2, y2, _) = brick

	return [(x, y) for y in range(y1, y2 + 1) for x in range(x1, x2 + 1)]

def brick_height(brick):
	return brick[1][2] - brick[0][2] + 1

def num_fallen_bricks(supporters, supportees, missing_brick):
	missing_bricks = { missing_brick }
	falling_bricks = missing_bricks

	while falling_bricks:
		bricks_supportees = set(supportee for brick in falling_bricks for supportee in supportees.get(brick, set()))
		
		falling_bricks = set(supportee for supportee in bricks_supportees if all(supporter in missing_bricks for supporter in supporters[supportee]))

		missing_bricks |= falling_bricks

	return len(missing_bricks) - 1

def main():
	bricks = []

	for line in sys.stdin:
		brick = line.split("~")
		bricks.append((tuple(int(c) for c in brick[0].split(",")), tuple(int(c) for c in brick[1].split(","))))

	bricks.sort(key = lambda brick: brick[0][2])

	supporters = {}
	supportees = {}

	ground = {}
	for brick in bricks:
		brick_blocks = brick_blocks_2D(brick)

		grounds = [ground[block] for block in brick_blocks if block in ground]

		max_ground = max([ground[1] for ground in grounds] + [0])

		supporters[brick] = set(ground[0] for ground in grounds if ground[1] == max_ground)

		for supporter in supporters[brick]:
			supportees.setdefault(supporter, set())
			supportees[supporter].add(brick)

		for x, y in brick_blocks:
			ground[(x, y)] = (brick, max_ground + brick_height(brick))

	print(sum(num_fallen_bricks(supporters, supportees, brick) for brick in bricks))


if __name__ == "__main__":
	main()