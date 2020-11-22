def evalHand(deck):
    faces = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for value in deck:
        face = value % 13
        faces[face] += 1

    suits = [0,0,0,0]
    for value in deck:
        suit = value // 13
        suits[suit] += 1

    if faces.count(2) == 1 and faces.count(1) == 3:
        return 'pair: 1''
    elif faces.count(2) == 2 and faces.count(1) == 1:
        return 'Two pairs: 2'
    elif faces.count(3) == 1 and faces.count(1) == 2:
        return 'THREE_OF_A_KIND: 3'
    elif faces.count(3) == 1 and faces.count(2) == 1:
        return 'Full HOuse: 6'
    elif faces.count(4) == 1 and faces.count(1) == 1:
        return 'FOUR_OF_A_KIND: 7'
    elif faces.count(1) == 5:
        pos = faces.index(1)
        if faces[pos:pos+5] == [1,1,1,1,1] or faces[pos:pos+13] == [1,0,0,0,0,0,0,0,0,1,1,1,1]:
            return 'STRAIGHT:4'
    else:
        return 'Nothing: 0'
    if suits.count(5) == 1 and suits.count(1) == 0:
        return 'FLUSH: 5'
    if suits.count(5) == 1 and faces.count(1) == 5:
        pos = faces.index(1)
        if faces[pos:pos + 5] == [1, 1, 1, 1, 1] or faces[pos:pos + 13] == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]:
            return 'STRAIGHT_FLUSH: 8'
 
 inputs = '9D 8C 8S 8H 9S'
 