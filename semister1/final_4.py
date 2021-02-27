a = ['AS', '13S', '13S','6S', '9S']
#check legal deck
if len(set(a)) != len(a):
    print('illegal deck!')
else:
    print('deck is valid')

#obtain deck info
point = [i[0:-1] for i in a]
adj_point = [int(x) if x!='A' else 14 for x in point]
suit = [i[-1] for i in a]
print('adj_point =\n',adj_point)
print('suit =\n',suit)

"""
get statistic of point & suit counts
deck example:　['AD', '13C', '13S','6H', '9S']
suit count  = [0, 3, 1, 0, 0, 0]
    one-time for 3, two-times for 1(->S)
point_count = [9, 3, 1, 0, 0, 0]
    3 diff points in the deck, 1 for twice
"""
sCounts = [0]*6
pCounts = [0]*6
for i in ['S','H','D','C']:
    sCounts[suit.count(i)] = sCounts[suit.count(i)]+1
for j in range(2,15):
    pCounts[adj_point.count(j)] = pCounts[adj_point.count(j)]+1
print('pCounts =',pCounts)
print('sCounts =',sCounts)

#straight examine
def isStraight(adj_point):
    adj_point.sort()
    if max(adj_point)==14 and min(adj_point)!=10:
        for i in range(len(adj_point)):
            if adj_point[i]<10:
                adj_point[i]+=13
    #check straight
    for i in range(len(adj_point)-1):
        if adj_point[i]+1 != adj_point[i+1]:
            return False
    return True

print(isStraight(adj_point))

#final examine
if sCounts[5]==1 and isStraight(adj_point)==True:
    print('Straight flush')
elif pCounts[4]==1:
    print('Four of a kind')
elif pCounts[3]==1 and pCounts[2]==1:
    print('Full House')
elif sCounts[5]==1:
    print('Flush')
elif isStraight(adj_point)==True:
    print('Straight')
elif pCounts[3]==1:
    print('Three of a kind')
elif pCounts[2]==2:
    print('Two pair')
elif pCounts[2]==1:
    print('One pair')
else:
    print('no kind')
