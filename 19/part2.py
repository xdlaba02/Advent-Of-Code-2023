import sys
import re
import copy

def parse_workflows(input):
	workflows = {}

	workflow_regex = re.compile(r"^(?P<name>[a-z]+){(?P<rules>.+)}$")
	rule_regex     = re.compile(r"^(?P<param>(x|m|a|s))(?P<operation>(<|>))(?P<value>\d+):(?P<workflow>([a-z]+|A|R))$")

	while line := input.readline().strip():
		line_match = workflow_regex.match(line)
		name = line_match.group("name")
		rules = line_match.group("rules").split(",")

		rule_list = []

		for rule in rules[:-1]:
			rule_match = rule_regex.match(rule)
			param = rule_match.group("param")
			operation = rule_match.group("operation")
			value = rule_match.group("value")
			workflow = rule_match.group("workflow")

			rule_list.append((param, operation, int(value), workflow))

		default_workflow = rules[-1]

		workflows[name] = (rule_list, default_workflow)

	return workflows

def evaluate_interval(interval):
	return max((interval[1] - interval[0] + 1), 0)

def evaluate_intervals(intervals):
	return evaluate_interval(intervals["x"]) * evaluate_interval(intervals["m"]) * evaluate_interval(intervals["a"]) * evaluate_interval(intervals["s"])

def slice_interval(interval, operation, value):
	if operation == "<":
		return ((interval[0], min(interval[1], value - 1)), (max(interval[0], value), interval[1]))
	
	if operation == ">":
		return ((max(interval[0], value + 1), interval[1]), (interval[0], min(interval[1], value)))

def score_workflows(workflows, workflow, intervals):
	if workflow == "A":
		return evaluate_intervals(intervals)
	
	if workflow == "R":
		return 0
	
	rules, default = workflows[workflow]

	intervals_copy = copy.copy(intervals)

	score = 0

	for param, operation, value, rule_workflow in rules:
		sliced_interval = slice_interval(intervals_copy[param], operation, value)
		intervals_copy[param] = sliced_interval[0]
		score += score_workflows(workflows, rule_workflow, intervals_copy)
		intervals_copy[param] = sliced_interval[1]

	score += score_workflows(workflows, default, intervals_copy)

	return score

def main():
	workflows = parse_workflows(sys.stdin)
	score = score_workflows(workflows, "in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}) 
	print(score)

if __name__ == "__main__":
	main()