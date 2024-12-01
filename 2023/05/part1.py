import sys

def parse_map(input):
	conversion_map = []

	input.readline()
	while line := input.readline().strip():
		conversion_map.append(tuple(map(int, line.split())))

	return conversion_map

def map_function(map, value):
	for dst_range_start, src_range_start, range_len in map:
		if src_range_start <= value <= src_range_start + range_len:
			return value - src_range_start + dst_range_start
		
	return value

def main():
	seeds = [int(seed_str) for seed_str in sys.stdin.readline().split(":")[1].split()]

	sys.stdin.readline()

	seed_to_soil            = parse_map(sys.stdin)
	soil_to_fertilizer      = parse_map(sys.stdin)
	fertilizer_to_water     = parse_map(sys.stdin)
	water_to_light          = parse_map(sys.stdin)
	light_to_temperature    = parse_map(sys.stdin)
	temperature_to_humidity = parse_map(sys.stdin)
	humidity_to_location    = parse_map(sys.stdin)
	
	def seed_to_location(seed):
		soil        = map_function(seed_to_soil, seed)
		fertilizer  = map_function(soil_to_fertilizer, soil)
		water       = map_function(fertilizer_to_water, fertilizer)
		light       = map_function(water_to_light, water)
		temperature = map_function(light_to_temperature, light)
		humidity    = map_function(temperature_to_humidity, temperature)
		location    = map_function(humidity_to_location, humidity)
		return location
	
	locations = [seed_to_location(seed) for seed in seeds]

	print(min(locations))

if __name__ == "__main__":
	main()