def convertPoint(card):
    face = ['14','2','3','4','5','6','7','8','9','10','11','12','13']
    point = [14,2,3,4,5,6,7,8,9,10,11,12,13]
    index = face.index(card)
    return point[index]

def straight(point):
    point.sort()
    if (max(point)==14 and min(point)!=10):
        for i in range(5):
            if point[i]<10:
                point[i]=point[i]+13
    point.sort()
#    print('sorted_point', point)
    for i in range(4):
        if point[i] != point[i+1]-1:
            return 0
    return 1

def compute(cards):
    p = [convertPoint(c[0:-1]) for c in cards]
    f = [c[-1] for c in cards]
#    print('f=%s, p=%s' %(f,p)) 
    print(getGrade(p,f))

def getGrade(point, color):
    f = [0,0,0,0,0,0]
    p = [0,0,0,0,0,0]
    for i in ['S','H','D','C']:
        f[color.count(i)] = f[color.count(i)]+1
    for j in range(2, 15):
        p[point.count(j)] = p[point.count(j)]+1

#    print('f=%s, p=%s' %(f,p))
    if straight(point)==1 and f[5]==1:
        return 8        #同花順
    if p[4]==1:
        return 7    #四條
    if p[3]==1 and p[2]==1:
        return 6    #葫蘆
    if f[5]==1:
        return 5    #同花
    if straight(point)==1:
        return 4    #順子
    if p[3]==1:
        return 3    #3條
    if p[2]==2:
        return 2    #2對
    if p[2]==1:
        return 1    #1對
    else:
        return 0

a = ['9D', '13C', '13S','6H', '9S']
#a = input().split()
compute(a)
