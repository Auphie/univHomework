def convertPoint(card):
    face = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    index = face.index(card)
    return point[index]

def computeWinner(player_score, score_comp):
    if player_score > score_comp:
        return('player wins')
    elif player_score == score_comp:
        return("It's a tie")
    else:
        return('computer wins')

init_player = input()
init_comp = input()
score_player = convertPoint(init_player)
score_comp = convertPoint(init_comp)
chase_stop = 0

while score_player <= 10.5:
    if input() == 'Y':
        score_player += convertPoint(input())
        if chase_stop == 0:
            if (score_comp <= 8 or score_comp < score_player < 10.5):
                chase_comp = input()
                score_comp += convertPoint(chase_comp)
            else:
                chase_stop += 1
    else:
        break

while (score_comp <= 8 or score_comp < score_player < 10.5):
    if chase_stop == 0:
        chase_comp = input()
        score_comp += convertPoint(chase_comp)
    else:
        break

score_player = 0 if score_player>10.5 else score_player
score_comp = 0 if score_comp>10.5 else score_comp
print('%.1f vs. %.1f' %(score_player, score_comp))
result = computeWinner(score_player, score_comp)
print(result)