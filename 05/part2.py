import sys

def parse_map(input):
	conversion_map = []

	input.readline()
	while line := input.readline().strip():
		conversion_map.append(tuple(map(int, line.split())))

	return conversion_map

def intersect(a, b):
	a_start, a_length = a
	a_end = a_start + a_length

	b_start, b_length = b
	b_end = b_start + b_length

	intersection_start  = max(a_start, b_start)
	intersection_end    = min(a_end, b_end)
	intersection_length = intersection_end - intersection_start

	return (intersection_start, intersection_length)

def subtract(a, b):
	a_start, a_length = a
	a_end = a_start + a_length

	b_start, b_length = b
	b_end = b_start + b_length

	difference = []

	if a_start < b_start:
		difference.append((a_start, b_start - a_start))

	if a_end > b_end:
		difference.append((b_end, a_end - b_end))

	return difference

def map_ranges(map, unmapped_ranges):
	mapped_ranges = []

	for dst_range_start, src_range_start, range_len in map:

		rest_of_unmapped_ranges = []

		for unmapped_range in unmapped_ranges:
			intersection_start, intersection_length = intersect(unmapped_range, (src_range_start, range_len))

			if intersection_length > 0:

				mapped_ranges.append((intersection_start - src_range_start + dst_range_start, intersection_length))

				rest_of_unmapped_ranges += subtract(unmapped_range, (src_range_start, range_len))
			else:
				rest_of_unmapped_ranges.append(unmapped_range)

		unmapped_ranges = rest_of_unmapped_ranges

	return mapped_ranges + unmapped_ranges

def main():
	seed_line = sys.stdin.readline().split(":")[1].split()

	seed_ranges = [(int(seed_start), int(len)) for seed_start, len in zip(seed_line[::2], seed_line[1::2])]

	sys.stdin.readline()

	seed_to_soil            = parse_map(sys.stdin)
	soil_to_fertilizer      = parse_map(sys.stdin)
	fertilizer_to_water     = parse_map(sys.stdin)
	water_to_light          = parse_map(sys.stdin)
	light_to_temperature    = parse_map(sys.stdin)
	temperature_to_humidity = parse_map(sys.stdin)
	humidity_to_location    = parse_map(sys.stdin)
	
	def seeds_to_location_ranges(seed_ranges):
		soil_ranges         = map_ranges(seed_to_soil, seed_ranges)
		fertilizer_ranges   = map_ranges(soil_to_fertilizer, soil_ranges)
		water_ranges        = map_ranges(fertilizer_to_water, fertilizer_ranges)
		light_ranges        = map_ranges(water_to_light, water_ranges)
		temperature_ranges  = map_ranges(light_to_temperature, light_ranges)
		humidity_ranges     = map_ranges(temperature_to_humidity, temperature_ranges)
		location_ranges     = map_ranges(humidity_to_location, humidity_ranges)
		return location_ranges
	
	location_ranges = seeds_to_location_ranges(seed_ranges)

	print(min([range_begin for range_begin, range_end in location_ranges]))

if __name__ == "__main__":
	main()