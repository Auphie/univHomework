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

content_counts =[]

for item in (a,b,c,d,e):
    content_counts.append(cal_counts(item, keywords))

result = sorted(content_counts, key=lambda x: x.get('counts'), reverse=True)

def toNotify(text, keywords):
    text.replace('Taipei', '---')
    print(text)


for i in result:
    toNotify(i['content'], keywords)