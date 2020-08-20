from random import randint

def square_cookie(board, i, j):
    if i-1 < 0 or j-1 < 0:
        return True
    elif board[i-1][j] == 0 and board[i-1][j-1] == 0 and board[i][j-1] == 0:
        return False
    else:
        return True

def not_blocked_cookie(board, i, j, band):
    if i-1 >= 0:
        if board[i-1][j] == 0:
            return True
    if j-1 >= 0:
        if board[i][j-1] == 0:
            return True
    if j+1 < len(board[0]) and band == True:
        if board[i][j+1] == 0:
            return True
    return False

def create_board():
    w, h = randint(10, 30), randint(10, 30)
    board = []
    for i in range(h):
        board.append([])
        for j in range (w):
            x = randint(0,1)
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
                        if not_blocked_cookie (board, i-1, j, True):
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
                        if not_blocked_cookie(board,i,j-1,False):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                    else:
                        if not_blocked_cookie(board, i-1, j, True) and not_blocked_cookie(board, i-1, j, False):
                            board[i].append(1)
                        else:
                            board[i].append(0)
                elif i != h-1:
                    if board[i-1][j] == 0 and not_blocked_cookie(board, i-1, j, True):
                        board[i].append(1)
                    elif board[i-1][j] == 1:
                        board[i].append(1)
                    else:
                        board[i].append(0)

    for i in range(len(board)):
        print(board[i])
create_board()
                        
