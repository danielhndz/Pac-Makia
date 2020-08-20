def dfs_paths(board, graph, start, goal):
    if board[goal[0]][goal[1]] == 1 or board[goal[0]][goal[1]] == 'f':
        return False
    stack = [[start]]
    smaller = None
    while stack:
        path  = stack.pop()
        node = path[-1]
        for next in set(graph[node]) - set(path):
            if next == goal:
                if smaller == None:
                    smaller = path + [next]
                elif len(path+[next]) < len(smaller):
                    smaller = path + [next]
            else:
                if board[next[0]][next[1]] == 0 or board[next[0]][next[1]] == 'x':
                    stack.append(path+[next])
    if smaller is None:
        return False
    else:
        return smaller