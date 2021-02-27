import numpy as np 
import copy

def get_input(board):    
    for i in range(10):
        inputs = input()
        board[i] = [int(elm) for elm in inputs]
    return board

def valid_line(lines, player):
    if len(lines) < 5:
        return False
    for i in range(len(lines)-4):
        if i < (len(lines)-5) and ((lines[i:i+5]==player).sum()==5 and (lines[i+5]!=player)):
            return True
        if (i == (len(lines)-5)) and ((lines[i:i+5]==player).sum()==5):
            return True
    return False

def checkWinner(data, player):
    diagonalL = [np.diagonal(data, offset=i) for i in range(3-len(data),len(data)-3)]
    diagonalR = [np.fliplr(data).diagonal(offset=i)for i in range(3-len(data),len(data)-3)]
    for row in data:
        if valid_line(row, player):
            return True
    for col in data.T:
        if valid_line(col, player):
            return True
    for backslash in diagonalL:
        if valid_line(backslash, player):
            return True
    for slash in diagonalR:
        if valid_line(slash, player):
            return True
    return False

def winMove(data, player):
    tempBoard = copy.deepcopy(data)
    for x in range(10):
        for y in range(10):
            if tempBoard[x][y]==0:
                tempBoard[x][y] = player
                if checkWinner(tempBoard, player)==True:
                    return x, y
                else:
                    tempBoard[x][y]=0

def check_result(data):
    result = ''
    p1_moves = (data==1).sum()
    p2_moves = (data==2).sum()
    nextPlayer = 1 if p1_moves == p2_moves else 2
    is_finished = 0
    for player in (1,2):
        if checkWinner(data, player)==True:
            is_finished = 1
            result='{} win'.format(player)
    if (data==0).sum()==0:
        result = 'tie'
    elif is_finished == 0:
        x, y = winMove(data, nextPlayer)
        result = str(x)+str(y)
    return result

board = np.zeros((10,10))
data = get_input(board)

result = check_result(data)
print(result)