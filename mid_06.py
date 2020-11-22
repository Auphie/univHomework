def transPoint(card):
    face = ['A','2','3','4','5','6','7','8','9','10','J','Q', 'K']
    color = ['S','H','D','C']
    point1 = [14,2,3,4,5,6,7,8,9,10,11,12,13]
    point2 = [1,2,3,4]
    f_index = face.index(card[0])
    c_index = color.index(card[1])
    return point1[f_index]*10 + point2[c_index]
    
def competeWinner(p_score,c_score,p_counts,c_counts):
    if (p_counts == 5 or p_score > c_score):
        print('Player X is winner')
    elif p_score < c_score:
        print('Player Y is winner')
    else:
        print('Draw game')

def main():
    player1 = ['7D', '7S', '8H', '8D', '9D']
    playerL1 = [transPoint(i) for i in player1]
    print(playerL1)

main()