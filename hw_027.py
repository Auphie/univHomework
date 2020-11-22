p1_points = 0
p2_points = 0

def convertPoint(card):
    face = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    index = face.index(card)
    return point[index]

def split_input(stream):
    splits = stream.split(' ')
    return splits

def chase_card(chase):
    bout = split_input(chase)
    p1_stop = 1
    p2_stop = 1
    p1_point = 0
    p2_point = 0
    if bout[0] == 0:
        p1_stop = 0
        p1_point = 0
        print('bout[0] pass')
        if bout[1] == 0:
            p2_stop = 0
            p2_point = 0
            print('bout[1] pass')
        else:
            p2_point = convertPoint(bout[2])
            print('bout[2] pass')
    else:
        p1_point = convertPoint(bout[1])
        if bout[2] == 0:
            p2_stop = 0
            p2_point = 0
            print('bout[3] pass')
        else:
            p2_point = convertPoint(bout[3])
            print('bout[4] pass')
    return p1_stop, p1_point, p2_stop, p2_point

def computeWinner(p1_scores, p2_scores):
    p1_scores = 0 if p1_scores > 21 else p1_scores
    p2_scores = 0 if p2_scores > 21 else p2_scores
    if p1_scores > p2_scores:
        print('Player X is Winner')
    elif p1_scores == p2_scores:
        print("It's a tie")
    else:
        print('Player Y is Winner')

    result_x = 'Bang!' if p1_scores ==0 else p1_scores
    result_y = 'Bang!' if p2_scores ==0 else p2_scores
    print('Player X $ %s'%result_x)
    print('Player Y $ %s'%result_y)

init_deck = input()
#init_deck = 'A K'
p1_points = convertPoint(split_input(init_deck)[0])
p2_points = convertPoint(split_input(init_deck)[1])
#print(p1_points, p2_points)

i = 0
while (i<4):
#    chase = split_input(input())
    chase = ['1','A','0']
    p1_stop, p1_point, p2_stop, p2_point = chase_card(chase)
    while p1_stop == 0 and p2_stop == 0:
        break
    else:
        print(p1_stop, p1_point, p2_stop, p2_point)
        p1_points += p1_point
        p2_points += p2_point
    i += 1

computeWinner(p1_points, p2_points)