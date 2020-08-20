from collections import deque

def shorted_path_bfs(board, graph, start, goal):
    if board[goal[0]][goal[1]] == 1 or board[goal[0]][goal[1]] == 'f':
        return False
    explored = []
    queue = deque([start])
    if start == goal:
        return True
    path = None
    while queue:
        if path == None:
            path = [queue.popleft()]
        else:
            path = queue.popleft()
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in explored and (board[neighbour[0]][neighbour[1]] == 0 or board[neighbour[0]][neighbour[1]] == 'x'):
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path
            explored.append(node)
    return False