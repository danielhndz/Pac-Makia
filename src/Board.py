from random import randint
from BFS import shorted_path_bfs
from Graph import list_ad

def validate_block(board, position):
    block = [position]
    neighbours = []
    if position[0]-1 >= 0:
        if board[position[0]-1][position[1]] == 1:
            neighbours.append((position[0]-1, position[1]))
            block.append((position[0]-1, position[1]))
    if position[0]+1 <= len(board)-1:
        if board[position[0]+1][position[1]] == 1:
            neighbours.append((position[0]+1, position[1]))
            block.append((position[0]+1, position[1]))
    if position[1]-1 >= 0:
        if board[position[0]][position[1]-1] == 1:
            neighbours.append((position[0], position[1]-1))
            block.append((position[0], position[1]-1))
    if position[1]+1 <= len(board[position[0]])-1:
        if board[position[0]][position[1]+1] == 1:
            neighbours.append((position[0], position[1]+1))
            block.append((position[0], position[1]+1))
    while len(neighbours) > 0:
        temp = []
        for neighbour in neighbours:
            if neighbour[0]-1 >= 0:
                if board[neighbour[0]-1][neighbour[1]] == 1 and (neighbour[0]-1, neighbour[1]) not in block:
                    temp.append((neighbour[0]-1, neighbour[1]))
                    block.append((neighbour[0]-1, neighbour[1]))
            if neighbour[0]+1 <= len(board)-1:
                if board[neighbour[0]+1][neighbour[1]] == 1 and (neighbour[0]+1, neighbour[1]) not in block:
                    temp.append((neighbour[0]+1, neighbour[1]))
                    block.append((neighbour[0]+1, neighbour[1]))
            if neighbour[1]-1 >= 0:
                if board[neighbour[0]][neighbour[1]-1] == 1 and (neighbour[0], neighbour[1]-1) not in block:
                    temp.append((neighbour[0], neighbour[1]-1))
                    block.append((neighbour[0], neighbour[1]-1))
            if neighbour[1]+1 <= len(board[neighbour[0]])-1:
                if board[neighbour[0]][neighbour[1]+1] == 1 and (neighbour[0]-1, neighbour[1]) not in block:
                    temp.append((neighbour[0], neighbour[1]+1))
                    block.append((neighbour[0], neighbour[1]+1))
        neighbours = list(temp)
    block.sort()
    for obs in block:
        if obs[0]-1 >= 0 and (obs[0]-1, obs[1]) not in block:
            board[obs[0]-1][obs[1]] = 0
        if obs[0]+1 <= len(board)-1 and (obs[0]+1, obs[1]) not in block:
            board[obs[0]+1][obs[1]] = 0
        if obs[1]-1 >= 0 and (obs[0], obs[1]-1) not in block:
            board[obs[0]][obs[1]-1] = 0
        if obs[1]+1 <= len(board[obs[0]])-1 and (obs[0], obs[1]+1) not in block:
            board[obs[0]][obs[1]+1] = 0
        if obs[0]-1 >= 0 and obs[1]+1 <= len(board[obs[0]])-1 and (obs[0]-1, obs[1]+1) not in block:
            board[obs[0]-1][obs[1]+1] = 0
        if obs[0]+1 <= len(board)-1 and obs[1]+1 <= len(board[obs[0]])-1 and (obs[0]+1, obs[1]+1) not in block:
            board[obs[0]+1][obs[1]+1] = 0
        if obs[0]+1 <= len(board)-1 and obs[1]-1 <= 0 and (obs[0]+1, obs[1]-1) not in block:
            board[obs[0]+1][obs[1]-1] = 0
        if obs[0]-1 <= 0 and obs[1]-1 <= 0 and (obs[0]-1, obs[1]-1) not in block:
            board[obs[0]-1][obs[1]-1] = 0
    min_row = min(block, key = lambda row: block[0])[0]
    max_row = max(block, key = lambda row: block[0])[0]
    min_col = min(block, key = lambda col: block[0])[1]
    max_col = max(block, key = lambda col: block[0])[1]
    visited = []
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if board[i][j] == 0 and (i, j) not in visited:
                visited.append((i, j))
                temp = [(i, j)]
                neighbours = []
                if min_row <= i-1:
                    if board[i-1][j] == 0 and (i-1, j) not in visited:
                        visited.append((i-1, j))
                        neighbours.append((i-1, j))
                if i+1 <= max_row:
                    if board[i+1][j] == 0 and (i+1, j) not in visited:
                        visited.append((i+1, j))
                        neighbours.append((i+1, j))
                if min_col <= j-1:
                    if board[i][j-1] == 0 and (i, j-1) not in visited:
                        visited.append((i, j-1))
                        neighbours.append((i, j-1))
                if j+1 <= max_col:
                    if board[i][j+1] == 0 and (i, j+1) not in visited:
                        visited.append((i, j+1))
                        neighbours.append((i, j+1))
                temp += neighbours
                while len(temp) < len(block):
                    temp2 = []
                    for neighbour in neighbours:
                        if min_row <= neighbour[0]-1 and neighbour[0]-1 <= max_row:
                            if board[neighbour[0]-1][neighbour[1]] == 0 and (neighbour[0]-1, neighbour[1]) not in visited:
                                visited.append((neighbour[0]-1, neighbour[1]))
                                temp2.append((neighbour[0]-1, neighbour[1]))
                        if min_row <= neighbour[0]+1 and neighbour[0]+1 <= max_row:
                            if board[neighbour[0]+1][neighbour[1]] == 0 and (neighbour[0]+1, neighbour[1]) not in visited:
                                visited.append((neighbour[0]+1, neighbour[1]))
                                temp2.append((neighbour[0]+1, neighbour[1]))
                        if min_col <= neighbour[1]-1 and neighbour[1]-1 <= max_col:
                            if board[neighbour[0]][neighbour[1]-1] == 0 and (neighbour[0], neighbour[1]-1) not in visited:
                                visited.append((neighbour[0], neighbour[1]-1))
                                temp2.append((neighbour[0], neighbour[1]-1))
                        if min_row <= neighbour[0]-1 and neighbour[0]-1 <= max_row:
                            if board[neighbour[0]][neighbour[1]+1] == 0 and (neighbour[0], neighbour[1]+1) not in visited:
                                visited.append((neighbour[0], neighbour[1]+1))
                                temp2.append((neighbour[0], neighbour[1]+1))
                    neighbours = list(temp2)
                    temp += neighbours
                    if len(neighbours) == 0:
                        break
                if len(neighbours) == 0 and len(temp) < len(block):
                    for k in temp:
                        board[k[0]][k[1]] = 1                
    return board, block

def validate_blocks(board):
    blocks = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                position = (i, j)
                break
        break
    board, block = validate_block(board, position)
    blocks += block
    flag1 = True
    while flag1:
        flag2 = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1 and (i, j) not in blocks:
                    position, flag2 = (i, j), True
                    break
        if flag2:
            board, block = validate_block(board, position)
            blocks += block
        else:
            flag1 = False
    return board

def square_cookie(board, i, j):
    if i-1 < 0 or j-1 < 0:
        return True
    elif board[i-1][j] == 0 and board[i-1][j-1] == 0 and board[i][j-1] == 0:
        return False
    else:
        return True

def not_blocked_cookie(board, i, j, band):
    if i-1>=0:
        if board[i-1][j] == 0:
            return True 
    if j-1 >= 0:
        if board[i][j-1] == 0:
            return True
    if j+1 < len(board[i]) and band == True:
        if board[i][j+1] == 0:
            return True
    return False

def create_board(we = None, ha = None):
    if we == None and ha == None: 
        w, h = randint(7, 15), randint(7, 14)
    else:
        w, h = we, ha
    board = []
    for i in range(h):
        board.append([])
        for j in range(w):
            x = randint(0, 1)
            if x == 0:
                if square_cookie(board, i, j):
                    board[i].append(0)
                else:
                    board[i].append(1)
            else:
                if i == 0:
                    board[i].append(1)
                elif i == h-1 and j == 0:
                    if board[i-1][j] == 1:
                        board[i].append(1)
                    else:
                        if not_blocked_cookie(board, i-1, j, True):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                elif i == h-1 and j != 0:
                    if board[i-1][j] == 1 and board[i][j-1] == 1:
                        board[i].append(1)
                    elif board[i-1][j] == 0 and board[i][j-1] == 1:
                        if not_blocked_cookie(board, i-1, j, True):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                    elif board[i-1][j] == 1 and board[i][j-1] == 0:
                        if not_blocked_cookie(board, i, j-1, False):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                    else:
                        if not_blocked_cookie(board, i-1, j, True) and not_blocked_cookie(board, i, j-1, False):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                elif i != h-1:
                    if board[i-1][j]==0 and not_blocked_cookie(board, i-1, j, True):
                        board[i].append(1)
                    elif board[i-1][j] == 1:
                        board[i].append(1)
                    else:
                        board[i].append(0)
    board = validate_blocks(board)
    line_final = []
    for i in range(0, w):
        if i == 0:
            line_final.append("pacman")
        else:
            line_final.append(0)
    board.append(line_final)
    ghost = randint(1, 4)
    for i in range(ghost):
        position = (randint(0, len(board)-1), randint(0, len(board[0])-1))
        while True:
            if board[position[0]][position[1]] == 0:
                board[position[0]][position[1]] = 'f'
                break
            else:
                position = (randint(0, len(board)-1), randint(0, len(board[0])-1))
    return board

def main_board(we = None, ha = None):
    while True:
        board = create_board(we, ha)
        graph = list_ad(board)
        cookies, paths = 0, 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    cookies += 1
                    path = shorted_path_bfs(board, graph, (len(board)-1, 0), (i, j))
                    if path != False:
                        paths += 1
        if cookies == paths:
            return board