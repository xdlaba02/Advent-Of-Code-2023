import sys

def distance(total_time, hold_time):
	run_time = total_time - hold_time
	return hold_time * run_time

def main():
	times     = [int(time_str)     for time_str     in sys.stdin.readline().split(":")[1].split()]
	distances = [int(distance_str) for distance_str in sys.stdin.readline().split(":")[1].split()]

	multiplicant = 1
	
	for time, limit_distance in zip(times, distances):

		margin_of_error = 0

		for hold_time in range(time):
			if distance(time, hold_time) > limit_distance:
				margin_of_error += 1

		multiplicant *= margin_of_error

	print(multiplicant)

if __name__ == "__main__":
	main()