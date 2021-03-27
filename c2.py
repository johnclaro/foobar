from collections import namedtuple

Node = namedtuple('Node', ['x', 'y'])


def solution(src, dest):
    rows, cols = (8,8)
    board = init_board(rows, cols)
    edges = generate_edges(board)
    return 0


def init_board(rows, cols):
    board = {}
    square = 0
    for col in range(cols):
        for row in range(rows):
            node = Node(row, -col)
            board[node] = square
            square += 1
    return board


def generate_edges(board):
    edges = {}
    moves = (
            Node(-1, 2), Node(1, 2),
        Node(-2, 1),            Node(2, 1),
        Node(-2, -1),            Node(2, -1),
            Node(-2, -2), Node(1, -2),
    )
    for node in board.keys():
        for move in moves:
            x, y = move.x + node.x, move.y + node.y
            if (0 < x < 8) and (0 > y > -8):
                edge = (x, y)
                try:
                    edges[node].append(edge)
                except KeyError:
                    edges[node] = [edge]
    return edges

if __name__ == '__main__':
    output = solution(19, 36)
    print output
