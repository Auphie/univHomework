a = 'National Taipei University of Technology, Taipei_Tech!!!'
b = 'National Taiwan University of Science and Technology, Taiwan%sTech??'
c = 'Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology'
d = 'Department of Computer Science and Information Engineering, Taipei Tech'
e = 'Department of Computer Science and Information Engineering, [National Taiwan University]'
key = 'Taipei Tai Tech comPuTer Science engineer'
keywords = ['Taipei', 'Tai', 'Tech', 'comPuTer', 'Science', 'engineer']

def cal_counts(item, keywords):
    new_dict={}
    count=0
    for keyword in keywords:
        for seg in item.split():
            if keyword.lower() in seg.lower():
                count += 1
    new_dict['content'] = item
    new_dict['counts'] = count
    return new_dict

def toNotify(text, keywords):
    for keyword in keywords:
#        text.isupper() if 
        index = text.lower().find(keyword.lower(), 0)
        while index != -1:
            text = text.replace(text[index:index + len(keyword)], keyword.upper(), 1)
            index = text.lower().find(keyword.lower(), index + 1)
    print(text)

content_counts =[]

num = input()
strings = []
for i in range(int(num)):
    string = input()
    strings.append(string)

keywords = input().split()

for item in strings:
    content_counts.append(cal_counts(item, keywords))

result = sorted(content_counts, key=lambda x: x.get('counts'), reverse=True)

#print('content=',content_counts)

for i in result:
    toNotify(i['content'], keywords)