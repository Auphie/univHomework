def convertPoint(card):
    if card in ('J','Q','K'):
        card = 0.5
    elif card == 'A':
        card = 1
    else: card
    return card

def convert2(card):
    face = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    index = face.index(card)
    return point[index]

def count_points(*card):
    tmp = list(card)
    point_sum = 0
    for i in tmp:
        point = float(convert2(i))
        point_sum += point
    return point_sum if point_sum <= 10.5 else 0

def computeWinner(player1, player2):
    print('%d' %player1)
    print('%d' %player2)
    if player1 > player2:
        print('A Win')
    elif player1 == player2:
        print('Tie')
    else:
        print('B Win')

card_1 = 'A'
card_2 = 'K'
card_3 = '10'
player1 = count_points(card_1, card_2, card_3)
card_4 = '5'
card_5 = '3'
card_6 = 'K'
player2 = count_points(card_4, card_5, card_6)
computeWinner(player1, player2)