def transPoint(card):
    face = ['A','2','3','4','5','6','7','8','9','10','J','Q', 'K']
    point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    c_index = face.index(card)
    return point[c_index]
    
def toChase(nextRound):
    print(nextRound)
    if nextRound[0] == 0:
        if nextRound[1] == 0:
            xChase = False
            yChase = False
            xPoint = 0
            yPoint = 0
        else:
            xChase = True
            yChase = False
            xPoint = nextRound[2]
            yPoint = 0
    else:
        if nextRound[2] == 0:
            xChase = False
            yChase = True
            xPoint = 0
            yPoint = nextRound[1]
        else:
            xChase = True
            yChase = True
            xPoint = nextRound[3]
            yPoint = nextRound[1]
    return xChase, yChase, xPoint, yPoint

def competeWinner(pX_score,pY_score,pX_counts,pY_counts):
    if (pY_counts == 5 or pY_score > pX_score):
        print('Player Y is winner')
    elif pY_score < pX_score:
        print('Player X is winner')
    else:
        print('Draw game')

def main():
    pX_score = 0
    pY_score = 0
    pX_counts = 0
    pY_counts = 0
    xChase = True
    yChase = True
    aRound = input().split()

    pX_score = transPoint(aRound[0])
    pX_counts += 1
    pY_score = transPoint(aRound[1])
    pY_counts += 1

    for i in range(4):
        while (pY_score == 0 or pX_score == 0  or (xChase==False and yChase==False)):
            break
        else:
            nextRound = input().split()
            data = [int(i) for i in nextRound]
            xChase, yChase, xPoint, yPoint = toChase(data)
            if yChase == True and pY_score != '0':
                pY_score += yPoint
                pY_counts += 1
                pY_score = 0 if pY_score > 11.5 else pY_score
            if xChase == True and pX_score != '0':
                pX_score += xPoint
                pX_counts += 1
                pX_score = 0 if pX_score > 11.5 else pX_score

    competeWinner(pX_score,pY_score,pX_counts,pY_counts)
    print('playerX_score=', pX_score)
    print('playerY_score=', pY_score)
    print('playerX_count=', pX_counts)
    print('playerY_count=', pY_counts)

main()