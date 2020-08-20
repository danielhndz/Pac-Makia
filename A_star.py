import queue

def heuristic(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def shorted_path_a_star(board, graph, start, goal):
    if board[goal[0]][goal[1]] == 1 or board[goal[0]][goal[1]] == 'f':
        return False
    explored = []
    priority_queue = queue.PriorityQueue()
    priority_queue.put((0 + heuristic(goal, start), [start]))
    while priority_queue.empty() == False:
        path = priority_queue.get()
        node = path[1][-1]
        if node == goal:
            return path[1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in explored and (board[neighbour[0]][neighbour[1]] == 0 or board[neighbour[0]][neighbour[1]] == 'x'):
                    new_path = list(path[1])
                    new_path.append(neighbour)
                    if board[neighbour[0]][neighbour[1]] == 'f':
                        priority_queue.put((float("inf"), new_path))
                    else:
                        priority_queue.put((path[0]+1+heuristic(goal, neighbour), new_path))
            explored.append(node)
        else:
            return False
    return False