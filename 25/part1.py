import sys
import random
import copy

def contract(graph, u, v):
	graph[u + v] = graph[u] + graph[v]

	for neighbor in graph[u]:
		graph[neighbor].remove(u)
		graph[neighbor].append(u + v)

	for neighbor in graph[v]:
		graph[neighbor].remove(v)
		graph[neighbor].append(u + v)

	graph[u + v] = [node for node in graph[u + v] if node not in [u, v, u + v]]

	graph.pop(u)
	graph.pop(v)

def karger_algorithm(graph):
	work_graph = copy.deepcopy(graph)

	while len(work_graph) > 2:
		u = random.choice(list(work_graph.keys()))
		v = random.choice(list(work_graph[u]))

		contract(work_graph, u, v)

	return work_graph


def main():
	graph = {}

	for line in sys.stdin:
		from_node, to_nodes_str = line.split(": ")
		to_nodes = to_nodes_str.split()

		graph.setdefault(from_node, [])
		graph[from_node] += to_nodes

		for to_node in to_nodes:
			graph.setdefault(to_node, [])
			graph[to_node].append(from_node)

	while True:
		result = karger_algorithm(graph)

		if len(result[list(result.keys())[0]]) <= 3:
			break

	a, b = result.keys()

	print((len(a) // 3) * (len(b) // 3))

if __name__ == "__main__":
	main()