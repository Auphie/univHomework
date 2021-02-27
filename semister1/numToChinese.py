def unit_digit3(num):
    rev_num = ''.join([i for i in num[::-1]])
    result = []
    label_1 = ['', '拾', '佰', '仟']
    result=''.join([y+x for x,y in zip(rev_num, label_1) if x !='零'])
    return result

def num_split(num):
    final = []
    trans = ['零', '壹', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖']
    units = ['', '萬', '億']
    numCh=''.join([trans[int(x)] for x in num])
    while numCh:
        final.append(units[0])
        final+=unit_digit3(numCh[-4:])
        units.pop(0)
        numCh = numCh[0:-4]
    result = ''.join([i for i in final[::-1]])
    return result

num='1100600'
print('num=', num)
print('Translate = ' + num_split(num) + '元')