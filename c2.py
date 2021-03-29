from collections import deque


def init_board(rows, cols):
    """Initializes dictionary with coordinates and its square number.

    Args:
        rows: An integer that represents the number of rows of a board.
        cols: An integer that represents the number of columns of a board.

    Returns:
        A dict mapping keys to the corresponding coordinate of a node
        represented as a tuple. Each row is represented with its square number.
    """
    board = {}
    node = 0
    for y in range(cols):
        for x in range(rows):
            board[x, -y] = node
            node += 1
    return board


def init_graph(board, rows, cols):
    """Initializes dictionary with nodes and its adjacent nodes that can be
    travelled to using a chess knight's moves.

    Args:
        board: The chessboard as a dictionary.
        rows: An integer that represents the number of rows of a board.
        cols: An integer that represents the number of columns of a board.

    Returns:
        A dict mapping keys to the corresponding coordinate of a node
        represented as a tuple. Each row is represented as a list the adjacent
        nodes.
    """
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
    # Loop through all possible points of the board
    for point, node in board.items():
        # Loop through all possible chess knight moves
        for move in moves:
            # Calculate difference between possible move and the current point
            x = move[0] + point[0]
            y = move[1] + point[1]
            # Only allow coordinates that are not outside the chessboard
            if 0 <= x < rows and 0 >= y > -cols:
                # Get the adjacent node's square number
                adjacent = board[x, y]
                try:
                    graph[node].append(adjacent)
                except KeyError:
                    graph[node] = [adjacent]
    return graph


def find_shortest_path(graph, src, dest):
    """Finds the shortest path between two nodes using breadth-first search.

    Args:
        graph: A dict mapping keys to the corresponding coordinate of a node
            represented as a tuple. Each row is represented with its square
            number.
        src: An integer representing the source node.
        dest: An integer representing the destination node.

    Returns:
        A list containing nodes that can be travelled to from the source node
        to the destination node
    """
    root = [[src]]
    # dequeue.popleft() has O(1) complexity whereas list.pop(0) has O(n)
    queue = deque(root)
    visited = set()
    while queue:
        # Get the first path in the queue
        path = queue.popleft()
        # Get the last node in the path
        node = path[-1]
        # Return shortest path if destination is reached
        if node == dest:
            return path
        # Check current node if visited in order not to recheck it
        elif node not in visited:
            # Loop adjacent node then construct new path and add to queue
            for adjacent_node in graph[node]:
                paths = list(path)
                paths.append(adjacent_node)
                queue.append(paths)
            # Mark the node as visited
            visited.add(node)
    return queue


def solution(src, dest):
    """Starts finding the solution to the dont-get-volunteered challenge.

    Args:
        src: An integer representing the source node.
        dest: An integer representing the destination node.

    Returns:
        An integer representing the smallest number of moves it will take to
        travel between the source square to the destination square using a
        chess knight's moves.
    """
    rows, cols = (8, 8)
    board = init_board(rows, cols)
    graph = init_graph(board, rows, cols)
    path = find_shortest_path(graph, src, dest)
    output = len(path) - 1
    return output


if __name__ == '__main__':
    import time
    start_time = time.time()
    xs = range(64)
    ys = range(64)
    outputs = []
    for x in xs:
        for y in ys:
            output = solution(x, y)
    print("--- %s seconds ---" % (time.time() - start_time))
