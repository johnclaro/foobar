from c2 import solution, init_board, init_graph


def test_given_solutions():
    assert solution(0, 1) == 3
    assert solution(19, 36) == 1


def test_corners():
    for xy in [
        (0, 63),
        (63, 0),
        (56, 7),
        (7, 56),
    ]:
        assert solution(xy[0], xy[1]) == 6


def test_graph():
    rows, cols = (8, 8)
    board = init_board(rows, cols)
    graph = init_graph(board)
    assert graph[0] == [10, 17]
    assert graph[10] == [0, 4, 16, 25, 20, 27]
