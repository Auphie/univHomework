def create_sized_list(size):
    a = [0]
    canvas = a * size
    return canvas

def segments(n):
    sets = []
    for i in range(n):
        segment = input()
        sets.append(segment.split(' '))
    return sets

def turn_one(sets):
    for segment in sets:
        for i in range(int(segment[0])+1, int(segment[1])+1):
            canvas[int(i)] = 1

canvas = create_sized_list(60000)
data = segments(int(input()))
#data = [[6,17], [0,13], [9,10]]
turn_one(data)
print(int(sum(canvas)))