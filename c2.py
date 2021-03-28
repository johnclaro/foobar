import time
from collections import deque


def init_board(rows, cols):
    board = {}
    node = 0
    for y in range(cols):
        for x in range(rows):
            board[x, -y] = node
            node += 1
    return board


def init_graph(board):
    graph = {}
    lshapes = (
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
        for lshape in lshapes:
            x = lshape[0] + point[0]
            y = lshape[1] + point[1]
            if 0 <= x < 8 and 0 >= y > -8:
                adjacent = board[x, y]
                try:
                    graph[node].append(adjacent)
                except KeyError:
                    graph[node] = [adjacent]
    return graph


def find_shortest_path(graph, src, dest):
    root = [[src]]
    queue = deque(root)
    visited = set()
    while queue:
        # Get the first path in the queue
        path = queue.popleft()
        # Get the last node in the path
        node = path[-1]
        # Stop if destination is reached
        if node == dest:
            return path
        # Check current node if visited in order not to recheck it
        elif node not in visited:
            # Loop adjacent node then construct new path and add to queue
            for adjacent_node in graph[node]:
                # TODO: Why is this list(path) and not [path]?
                paths = list(path)
                paths.append(adjacent_node)
                queue.append(paths)
            # Mark the node as visited
            visited.add(node)
    return queue


def solution(src, dest):
    rows, cols = (8, 8)
    board = init_board(rows, cols)
    graph = init_graph(board)
    path = find_shortest_path(graph, src, dest)
    output = len(path) - 1
    return output


if __name__ == '__main__':
    start_time = time.time()
    xs = range(64)
    ys = range(64)
    outputs = []
    for x in xs:
        for y in ys:
            output = solution(x, y)
    print("--- %s seconds ---" % (time.time() - start_time))
