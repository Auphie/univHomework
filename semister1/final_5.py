a = 'National Taipei University of Technology, Taipei_Tech!!!'
b = "National Taiwan University of Science and Technology, Taiwan's Tech??"
c = 'Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology'
d = 'Department of Computer Science and Information Engineering, Taipei Tech'
e = 'Department of Computer Science and Information Engineering, [National Taiwan University]'
key = 'Taipei Tai Tech comPuTer Science engineer'

""" create context's dict """
inputLines = []
nextNo=0
for line in (a,b,c,d,e):
    inputLines.append(line)

""" create keyword's list as lower_case """
keywords = [i.lower() for i in key.split()]
#print('keywords=\n',keywords)

""" count counts by keywords in each context """
dic_counts={}
for content in inputLines:
    counts=0
    for key in keywords:
        if key in content.lower():
""" use counts += s.lower().count(key) to sum counts """
            counts+=content.lower().count(key)
    dic_counts[content] = counts
#print('dic_counts=',dic_counts)

# dic_counts= {'National Taipei University of Technology, Taipei_Tech!!!': 6,
#  "National Taiwan University of Science and Technology, Taiwan's Tech??": 5,
#  'Department of Computer Science and Information Engineering, National
#   Taiwan University of Science and Technology': 6,
#  'Department of Computer Science and Information Engineering, Taipei Tech': 6,
#   'Department of Computer Science and Information Engineering,
#    [National Taiwan University]': 4}

""" for dict, sort by key counts by descend use lambda """
sorted_dic = dict(sorted(dic_counts.items(), key=lambda x:(x[1]), reverse=True))
#print('sorted_dic=',sorted_dic)

""" replace keywords to capital in strings """
for s in sorted_dic.keys():
    for keyword in keywords:
""" find(keyword, start, end) """
        keyIndex = s.lower().find(keyword,0)
""" find() none will produce -1, so use while to skip """
        while keyIndex >= 0:
#            print('keyword=%s, index=%s'%(keyword,keyIndex))
""" replace(old, new, replace_num) """
            s=s.replace(s[keyIndex:keyIndex+len(keyword)],keyword.upper(),1)
            keyIndex = s.lower().find(keyword.lower(), keyIndex + 1)
    print('result=\n',s)