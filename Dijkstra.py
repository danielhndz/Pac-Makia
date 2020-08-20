from BFS import shorted_path_bfs

def arr_distances(cookies, start):
    arr = []
    for cookie in cookies:
        arr.append((abs(start[0]-cookie[0])+abs(start[1]-cookie[1]), cookie))
    arr = sorted(arr, key = lambda arr: arr[0])
    return arr

def dijkstra(board, graph, start):
    cookies = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                cookies.append((i, j))
    distances = arr_distances(cookies, start)
    path = []
    while True:
        if len(path) == 0:
            current_path = shorted_path_bfs(board, graph, start, distances[0][1])
        else:
            current_path = shorted_path_bfs(board, graph, path[-1], distances[0][1])
        if current_path is True:
            if path[-1] in cookies:
                cookies.remove(path[-1])
        elif current_path is False:
            return False
        else:
            temp = list(cookies)
            for i in current_path:
                if i in cookies:
                    temp.remove(i)
            cookies = list(temp)
            if len(path) > 0:
                if path[-1] == current_path[0]:
                    path += current_path[1:]
                else:
                    path += current_path
            else:
                path += current_path
        if len(cookies) == 0:
            break
        distances = arr_distances(cookies, path[-1])
    return path