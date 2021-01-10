a = 'National Taipei University of Technology, Taipei_Tech!!!'
b = "National Taiwan University of Science and Technology, Taiwan's Tech??"
c = 'Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology'
d = 'Department of Computer Science and Information Engineering, Taipei Tech'
e = 'Department of Computer Science and Information Engineering, [National Taiwan University]'
key = 'Taipei Tai Tech comPuTer Science engineer'

#create context's dict
dic = {}
nextNo=0
for case in (a,b,c,d,e):
    dic[nextNo]=case
    nextNo+=1
print('dic=\n',dic)

#create keyword's list as lower_case
keywords = [i.lower() for i in key.split()]
print('keywords=\n',keywords)

#count counts by keywords in each context
dic_counts={}
for content in dic.values():
    counts=0
    for key in keywords:
        if key in content.lower():
            counts+=content.lower().count(key) #Important!
    dic_counts[content] = counts
print('dic_counts=',dic_counts)
"""
dic_counts= {'National Taipei University of Technology, Taipei_Tech!!!': 6,
  "National Taiwan University of Science and Technology, Taiwan's Tech??": 5,
  'Department of Computer Science and Information Engineering, National
   Taiwan University of Science and Technology': 6,
  'Department of Computer Science and Information Engineering, Taipei Tech': 6,
   'Department of Computer Science and Information Engineering,
    [National Taiwan University]': 4}
"""

#sort by key counts desc use lambda
sorted_dic = sorted(dic_counts.items(), key=lambda x:(x[1]), reverse=True)
print('sorted_dic=',sorted_dic)

