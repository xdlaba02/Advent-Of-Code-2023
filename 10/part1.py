import sys

direction = {
	"l":  (-1,  0),
	"r":  ( 1,  0),
	"t":  ( 0, -1),
	"b":  ( 0,  1),
}

adjacency = {
	"|": {direction["t"], direction["b"]},
	"-": {direction["l"], direction["r"]},
	"L": {direction["t"], direction["r"]},
	"J": {direction["t"], direction["l"]},
	"7": {direction["l"], direction["b"]},
	"F": {direction["r"], direction["b"]},
	"S": {direction["l"], direction["r"], direction["t"], direction["b"]}, 
}

def connected_tiles(pipes, pos):
	x, y = pos
	width, heigh = (len(pipes[y]), len(pipes))
	symbol = pipes[y][x]

	return [(x + dx, y + dy) for dx, dy in adjacency[symbol] if 0 <= x + dx < width and 0 <= y + dy < heigh] if symbol in adjacency else []
			
def get_start(pipes):
	for y, row in enumerate(pipes):
		for x, element in enumerate(row):
			if element == "S":
				return (x, y)

def get_start_symbol(pipes, start):
	start_connections = {connection for connection in connected_tiles(pipes, start) if start in connected_tiles(pipes, connection)}

	start_directions = {(dx, dy) for position in start_connections for dx, dy in direction.values() if (start[0] + dx, start[1] + dy) == position}

	for key, value in adjacency.items():
		if start_directions == value:
			return key

def main():
	pipes = [list(row.strip()) for row in sys.stdin]

	start = get_start(pipes)

	pipes[start[1]][start[0]] = get_start_symbol(pipes, start)

	position, prev_position = connected_tiles(pipes, start)[0], start

	len = 1
	while position != start:
		len += 1
		position, prev_position = [connection for connection in connected_tiles(pipes, position) if connection != prev_position][0], position

	print(len // 2)

if __name__ == "__main__":
	main()