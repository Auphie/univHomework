univ_info = {'NSYSU': ['NC', 'CT', 'NS', 'NM'], 'NTU': ['BC', 'NC', 'CT', 'NS'], 'NCCU': ['BC', 'NL', 'HL'], 'Providence': ['BC', 'NC'], 'NTHU': ['BC', 'NS']}

univ_info = {}
for i in range(5):
    s = input().split()
    univ_info[s[0]] = s[1:]
print(univ_info)
b = 'BC NS + CT HL'.split('+')
c = [x.strip() for x in b]

def filter_univ(c, univ_info):
    for k, v in univ_info.items():
        result = True
        for criterion in d.strip().split():
            if criterion not in v:
                result = False
        if result == True:
            print('result=', k)

for d in c:
    filter_univ(d, univ_info)