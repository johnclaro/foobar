from collections import deque


def solution(src, dest):
    rows, cols = (8, 8)
    board = initialize_board(rows, cols)
    graph = initialize_graph(board)
    path = find_shortest_path(graph, src, dest)
    output = len(path) - 1
    return output


def initialize_board(rows, cols):
    board = {}
    node = 0
    for col in range(cols):
        for row in range(rows):
            point = (row, -col)
            board[point] = node
            node += 1
    return board


def initialize_graph(board):
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


def find_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph[node]:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return queue


if __name__ == '__main__':
    xs = range(64)
    ys = range(64)
    outputs = []
    for x in xs:
        for y in ys:
            output = solution(x, y)
