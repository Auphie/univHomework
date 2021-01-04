import numpy as np 
import copy

def get_input(board):    
    for i in range(10):
        inputs = input()
        board[i] = [int(elm) for elm in inputs]
    return board

def checkWinner(data, player): 
    result = False
    diagonalL = np.data.diagonal()
    diagonalR = np.fliplr(data).diagonal()
    for row in range(len(data)-1):
        for col in range(len(data)-6):
            if (((data[row,col:col+5]==player).sum()==5 
            and (data[row,col+5]!=player))
            or
            ((data.T[row,col:col+5]==player).sum()==5 and (data.T[row,col+5]!=player))
            ):
                result =  True
    for row in range(len(diagonalL-6)):
        if ((diagonalL[row:row+5]==player).sum()==5 and (ddiagonalL[ro+5]!=player)):
            result =  True
        elif ((diagonalR[row:row+5]==player).sum()==5 and (ddiagonalR[ro+5]!=player)):
            result =  True
    return result
  
def winMove(data, player):
    tempBoard = copy.deepcopy(data)
    for x in range(3):
        for y in range(3):
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

def main():
    board = np.zeros((11,11))
    data = get_input(board)
    #data = np.array([[2, 1, 0],[2, 1, 0],[0,0,0]])
    result = check_result(data)
    print(result)

main()