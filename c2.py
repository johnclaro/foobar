def solution(src, dest):
    rows, cols = (8,8)
    board = init_board(rows, cols)
    graph = init_graph(board)
    for k,v in graph.items():
        print k, ':', v
    return 0


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
            (-1, 2), (1, 2),
        (-2, 1),            (2, 1),
        (-2, -1),            (2, -1),
            (-2, -2), (1, -2),
    )
    for point, node in board.items():
        for move in moves:
            x, y = move[0] + point[0], move[1] + point[1]
            if (0 < x < 8) and (0 > y > -8):
                edge = board[(x, y)]
                try:
                    graph[node].append(edge)
                except KeyError:
                    graph[node] = [edge]
    return graph

if __name__ == '__main__':
    solution(19, 36)
