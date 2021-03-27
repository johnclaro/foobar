from c2 import solution, init_board, init_graph


# def test_1():
#     assert solution(0, 1) == 3

# def test_2():
    # assert solution(19, 36) == 1

def test_graph():
    rows, cols = (8,8)
    board = init_board(rows, cols)
    graph = init_graph(board)
    assert graph[0] == [10, 17]
    assert graph[10] == [0, 4, 16, 20, 24, 27]