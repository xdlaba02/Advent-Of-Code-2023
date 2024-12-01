import math
import sys
import re

def read_configuration(input):
	rule_regex = re.compile(r"^(?P<input_module_type>(&|%)?)(?P<input_module_name>[a-z]+) -> (?P<output_modules>.*)$")
	
	configuration = {}

	for line in input:
		match = rule_regex.match(line)

		input_module_type = match.group("input_module_type")
		input_module_name = match.group("input_module_name")
		output_modules    = match.group("output_modules").split(", ")

		configuration[input_module_name] = (input_module_type, output_modules)

	return configuration

def initialize_state(configuration):
	state = {}

	for module_name, (module_type, output_modules) in configuration.items():
		if module_type == "%":
			state[module_name] = False

		for output_module_name in output_modules:
			if output_module_name in configuration and configuration[output_module_name][0] == "&":
				state.setdefault(output_module_name, {})[module_name] = False

	return state

def main_counter_module(configuration):
	for module_name, (_, output_modules) in configuration.items():
		if "rx" in output_modules:
			return module_name

def button_presses_to_rx(configuration):
	main_counter_module = main_counter_module(configuration)

	intervals = {module_name: None for module_name, (_, output_modules) in configuration.items() if main_counter_module in output_modules}

	state = initialize_state(configuration)

	num_button_presses = 0
	while not all(intervals.values()):
		num_button_presses += 1

		impulses = [("button", "broadcaster", False)]

		while impulses:

			previous_module_name, current_module_name, impulse_type = impulses.pop(0)

			if current_module_name == main_counter_module and impulse_type == True:
				if not intervals[previous_module_name]:
					intervals[previous_module_name] = num_button_presses
			
			if current_module_name in configuration:
				current_module_type, next_modules = configuration[current_module_name]

				if current_module_type == "%" and impulse_type == False:
					state[current_module_name] = not state[current_module_name]
					impulses += [(current_module_name, next_module, state[current_module_name]) for next_module in next_modules]

				if current_module_type == "&":
					state[current_module_name][previous_module_name] = impulse_type
					impulses += [(current_module_name, next_module, not all(state[current_module_name].values())) for next_module in next_modules]

				if current_module_type == "":
					impulses += [(current_module_name, next_module, impulse_type) for next_module in next_modules]

	return math.lcm(*intervals.values())


def main():
	configuration = read_configuration(sys.stdin)

	print(button_presses_to_rx(configuration))

if __name__ == "__main__":
	main()