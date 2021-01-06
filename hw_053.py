import numpy as np 
import copy

def get_input(board):    
    for i in range(10):
        inputs = input()
        board[i] = [int(elm) for elm in inputs]
    return board

def valid_line(lines, player):
    for i in range(len(lines)-5):
        if i < (len(lines)-4) and ((lines[i:i+5]==player).sum()==5 and (lines[i+5]!=player)):
            return True
        if (i == (len(lines)-4)) and ((row[i:i+5]==player).sum()==5):
            return True
    return False

def checkWinner(data, player):
    result = False
    diagonalL = data.diagonal()
    diagonalR = np.fliplr(data).diagonal()
    for row in data:
        result1 =  valid_line(row, player)
    for col in data.T:
        result2 =  valid_line(col, player)
    result3 = valid_line(diagonalL, player)
    result4 = valid_line(diagonalR, player)
    print('res1=%s, res2=%s, res3=%s, res4=%s'%(result1, result2, result3, result4))
    result = result or result2 or result3 or result4
    return result

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
#    elif is_finished == 0:
#        x, y = winMove(data, nextPlayer)
#        result = str(x)+str(y)
    return result

#board = np.zeros((10,10))
#data = get_input(board)
data = np.array([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]])
#result = check_result(data)

result = checkWinner(data, 2)
print(result)