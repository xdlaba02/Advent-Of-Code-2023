import sys
import re

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

def parse_parts(input):
	parts = []

	part_regex = re.compile(r"^{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}")

	while line := input.readline().strip():
		line_match = part_regex.match(line)
		x = line_match.group("x")
		m = line_match.group("m")
		a = line_match.group("a")
		s = line_match.group("s")

		parts.append({"x": int(x), "m": int(m), "a": int(a), "s": int(s)})

	return parts

def apply_rule(part, param, operation, value):
	if operation == "<":
		return part[param] < value
	
	if operation == ">":
		return part[param] > value

def part_accepted(part, workflows):
	workflow = "in"

	while workflow != "A" and workflow != "R":
		rules, default = workflows[workflow]

		for param, operation, value, rule_workflow in rules:
			if apply_rule(part, param, operation, value):
				workflow = rule_workflow
				break
		else:
			workflow = default

	return workflow == "A"

def main():
	workflows = parse_workflows(sys.stdin)
	parts     = parse_parts(sys.stdin)

	sum = 0

	for part in parts:
		if part_accepted(part, workflows):
			sum += part["x"] + part["m"] + part["a"] + part["s"]

	print(sum)

if __name__ == "__main__":
	main()