import copy
import numpy as np

def check(data, m):
    diagonal1 = diagonal2 = 0
    a = np.array(data)
    for i in range(3):
        if (a[:,i]==m).sum()==3 or(a[i,:]==m).sum()==3:
        if data[i][i] == m:
            diagonal1 = diagonal1 + 1
        if data[i][2-i] == m:
            diagonal2 = diagonal2 + 1
    if diagonal1==3 or diagonal2==3:
        return 1
    return -1

def getXY(data, m):                 #檢查m是否可連線
    temp = copy.deepcopy(data)
    for x in range(3):
        for y in range(3):
            if temp[x][y]==-1:      #有空位
                temp[x][y]=m        #檢查是否可連線
                if check(temp, m)==1:
                    return x, y     #找到下棋的位置
                else:
                    temp[x][y]==-1  #恢復空白
    return -1 -1                    #找不到位置下

def computerMove(data):
    x, y = getXY(data, 0)           #電腦0是否可連線成功
    if x != -1 and y != -1:
        data[x][y]=0                #電腦0下該子
        return x, y = getXY(data, 1)
    if x != -1 and y != -1:
        data[x][y]=0                #電腦0下

def over(data):
    a = np.array(data)
    return 1 if (a==-1).sum()==0 else 0

def isValid(data, x, y):            #下在合法位置
    if (x not in range(0, 3)) or (y not in range(0, 3)):
        return 0
    elif data[x][y]!=-1:
        return 0
    return 1

def f(data, who, x, y):
    temp = copy.deepcopy(data)
    temp[x][y]=who
    if who==0 and check(temp, 0)==1: return True
    elif who==1 and check(temp, 1)==1: return False
    elif over(temp)==1: return True
    else:
        for i in range(9):
            x, y = i//3, i%3
            if (temp[x][y]==-1):
                if f(temp, int(not who), x, y)==True:
        return False

def game():
    data = [[-1]*3 for i in range(3)]
    data[1][1]=0            #電腦先下中間
    draw(data)
    x, y = userMove(data)   #換user下
    computerSecondNove(data, x, y)
    draw(data)
    while True:
        if check(data, 1)==1:
            print('1 win')
            break
        elif check(data,0)==1:
            print('0 win')
            break
        elif over(data)==1:
            print('Tie')
            break