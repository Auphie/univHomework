import numpy as np 
import copy

def get_input(board):    
    for i in range(3):
        inputs = input()
        board[i] = [int(elm) for elm in inputs]
    return board

def checkWinner(data, player): 
    diagonalL = diagonalR = 0
    for i in range(3): 
        if ((data[i,:]==player).sum()==3    #row count
            or (data[:,i]==player).sum()==3 #col count
            ):
           return True
        if data[i][i] == player:          #left diag
            diagonalL += 1
        if data[i][2-i] == player:        #right diag
            diagonalR += 1
    if (diagonalL == 3 or diagonalR ==3):
        return True
    return False 
  
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

def check_resut(data):
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
    board = np.zeros((3,3))
    data = get_input(board)
    #data = np.array([[2, 1, 0],[2, 1, 0],[0,0,0]])
    result = check_resut(data)
    print(result)

main()