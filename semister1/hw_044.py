import json

def input_string():
    str_lists = []
    a = input()
    if int(a)==0:
        return('')
    else:
        for i in range(int(a)):
            inpStr = input()
            str_lists.append(inpStr)
        return str_lists

def split_input(b):
    splitted=[]
    tmp = b.split()
    for i in tmp:
        splitted.append(i)
    return splitted

def get_seperate_point(splitted):
    sep_point=[2]
    for i in range(3,len(splitted)):
        if splitted[i].isnumeric():
            sep_point.append(i)
    return sep_point

def make_info(splitted, sep):
    info={}
    item={}
    info['hours']=splitted[1]+'-'+splitted[2]
    for i in range(len(sep)-1):
        item_name = ' '.join(splitted[sep[i]+1 : sep[i+1]])
        item[item_name]='$'+splitted[sep[i+1]]
    info['items']=item
    return info

b='breakfast 7 11 breakfast burritos 60 pancakes 60'
c='lunch 11 3 hamburger 50'
d='dinner 3 10 spaghetti 80'

menu={}
str_lists = input_string()
for i in str_lists:
#for i in (b,c,d):
    splitted=split_input(i)
    sep = get_seperate_point(splitted)
    info = make_info(splitted, sep)
    menu[splitted[0]]=info


aa=json.dumps(menu,indent=2)
bb = aa.replace('\"','\'')
if len(menu)==0:
    print('menu = '+'{\n}')
else:
    print('menu = '+bb)