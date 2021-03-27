from termcolor import colored


moves = (
        (-1, 2), (1, 2),
    (-2, 1),            (2, 1),
    (-2, -1),            (2, -1),
        (-2, -2), (1, -2),
)


def solution(src, dest):
    rows, cols = (8,8)
    board = init_board(rows, cols)
    output = 0
    for move in moves:
        move_x, move_y = move
        src_x, src_y = board[src]
        dest_x, dest_y = board[dest]
        diff_x = move_x + src_x
        diff_y = move_y + src_y
        if (0 < diff_x < 8) and (0 > diff_y > -8):
            diff = (diff_x, diff_y)
            for cell, coordinate in board.items():
                if coordinate == diff and coordinate == board[dest]:
                    output += 1
    return output


def init_board(rows, cols):
    board = {}
    cell = 0
    for col in range(cols):
        for row in range(rows):
            coordinate = (row, -col)
            board[cell] = coordinate
            cell += 1
    return board


if __name__ == '__main__':
    output = solution(0, 1)
    print output
