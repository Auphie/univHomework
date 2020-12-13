def input_univInfo(univ_num):
    univ_info = {}
    for i in range(int(univ_num)):
        info = input().split(' ',1)
        univ_info[info[0]] = info[1]
    return univ_info

def input_choice(selections):
    considerations = {}
    for i in range(int(selections)):
        temp= input().split('+')
        univ_criteria = [crit.strip() for crit in temp]
        considerations[i]=univ_criteria
    return considerations

def filter_univ(case,univ_info):
    options = [i.split() for i in case]
    for criteria in options:
        for univ in univ_info.items():
            result=1
#            print('univ[1]=',univ[1])
            for criterion in criteria:
#                print('criterion=',criterion)
                if criterion not in univ[1]:
                    result*=0
            if result == 1:
                print(univ[0], end=' ')
    print()

#univ_info = {'NSYSU': 'NC CT NS NM', 'NTU': 'BC NC CT NS', 'NCCU': 'BC NL HL', 'Providence': 'BC NC', 'NTHU': 'BC NS'}
#considerations = {0: ['BC NS', 'CT HL'], 1: ['NM', 'BC NL', 'BC NC']}

def main():
    univ_num = input()
    univ_info = input_univInfo(int(univ_num))
    selections = input()
    considerations = input_choice(int(selections))
    for case in considerations.values():
        filter_univ(case,univ_info)

main()