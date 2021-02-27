def create_list():
    lottery = {}
#    first_no = '41482012'
    first_no = input()
    lottery[first_no]=10000000
#    second_no = '58837976'
    second_no = input()
    lottery[second_no]=2000000
#    normal_no = ['20379435', '47430762', '36193504']
    normal_no = input().split()
    for number in normal_no:
        for seg in range(8,2,-1):
            if seg == 8: lottery[number[-seg:]]=200000
            elif seg==7: lottery[number[-seg:]]=40000
            elif seg==6: lottery[number[-seg:]]=10000
            elif seg==5: lottery[number[-seg:]]=4000
            elif seg==4: lottery[number[-seg:]]=1000
            elif seg==3: lottery[number[-seg:]]=200
#    extra_no = ['693', '043', '425']
    extra_no = input().split()
    for no in extra_no:
        lottery[no] = 200
    return lottery

def check_result(lotto_list, check_no):
    result = 0
    if len(check_no) <= 2:
        return 0
    elif check_no in lotto_list.keys():
        result = lotto_list[check_no]
    else:
        result += check_result(lotto_list, check_no[1:])
    return result

#lotto_list = {'45698621': 10000000, '19614436': 2000000, '96182420': 200000, '47464012': 200000, '62781818': 200000, '6182420': 40000, '7464012': 40000, '2781818': 40000, '182420': 10000, '464012': 10000, '781818': 10000, '82420': 4000, '64012': 4000, '81818': 4000, '2420': 1000, '4012': 1000, '1818': 1000, '928': 200, '899': 200, '118': 200, '420': 200, '012': 200, '818': 200}
#ticket_list = ['12342411','12341818']
def main():
    total_prize = 0
    lotto_list = create_list()
    ticket_num = input()
    ticket_list = [input() for i in range(int(ticket_num))]
    for check_no in ticket_list:
        total_prize += check_result(lotto_list, check_no)
    print(total_prize)

main()