input_univ1='NSYSU NC CT NS NM'
input_univ2='NTU BC NC CT NS'
input_univ3='NCCU BC NL HL'
input_univ4='Providence BC NC'
input_univ5='NTHU BC NS'
input_request1='BC NS + CT HL'       #case1. '+'= or, ' '= and
input_request2='NM + BC NL + BC NC'  #case2
"""
univ_info = {}
for i in range(5):
    s = input().split()
    univ_info[s[0]] = s[1:]
print(univ_info)
"""
univ_info = {'NSYSU': ['NC', 'CT', 'NS', 'NM'], 'NTU': ['BC', 'NC', 'CT', 'NS'], 'NCCU': ['BC', 'NL', 'HL'], 'Providence': ['BC', 'NC'], 'NTHU': ['BC', 'NS']}

def filter_univ(criteria, univ_info):
    for k, v in univ_info.items():  #list univ to be examed
        result = 1  
        for criterion in criteria:  #percise query
            if criterion not in v:
                result *= 0 # to verify 'and' condition
        if result == 1:
            print(k, end=' ')

for request in (input_request1, input_request2):
    print('\nresult = ', end='')
    options = request.split('+')
    for criteria in options:    #to practice 'or' query
        filter_univ(criteria.split(), univ_info)    #precise query