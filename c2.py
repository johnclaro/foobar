import time
from collections import deque


def solution(src, dest):
    rows, cols = (8, 8)
    board = init_board(rows, cols)
    graph = init_graph(board)
    path = find_shortest_path(graph, src, dest)
    output = len(path) - 1
    return output


def init_board(rows, cols):
    board = {}
    node = 0
    for col in range(cols):
        for row in range(rows):
            point = (row, -col)
            board[point] = node
            node += 1
    return board


def init_graph(board):
    graph = {}
    moves = (
        (-1, 2),
        (-2, 1),
        (1, 2),
        (2, 1),
        (-2, -1),
        (-1, -2),
        (2, -1),
        (1, -2),
    )
    for point, node in board.items():
        for move in moves:
            x, y = move[0] + point[0], move[1] + point[1]
            if (0 <= x < 8) and (0 >= y > -8):
                edge = board[(x, y)]
                try:
                    graph[node].append(edge)
                except KeyError:
                    graph[node] = [edge]
    return graph


def find_shortest_path(graph, src, dest):
    root = [[src]]
    nodes = deque(root)
    visited = set()
    while nodes:
        # Get the first path in the nodes
        path = nodes.popleft()
        # Get the last node in the path
        node = path[-1]
        # Stop if destination is reached
        if node == dest:
            return path
        # Check current node if visited in order not to recheck it
        elif node not in visited:
            # Loop adjacent nodes then construct new path and add to nodes
            for adj_node in graph[node]:
                paths = list(path)
                paths.append(adj_node)
                nodes.append(paths)
            # Mark the node as visited
            visited.add(node)
    return nodes


if __name__ == '__main__':
    start_time = time.time()
    xs = range(64)
    ys = range(64)
    outputs = []
    for x in xs:
        for y in ys:
            output = solution(x, y)
    print("--- %s seconds ---" % (time.time() - start_time))
