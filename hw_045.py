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
    sorted_lottery = {}
    for k in sorted(lottery, key=len, reverse=True):
        sorted_lottery[k] = lottery[k]
    return sorted_lottery

def check_result(prize_list, checking_no):
    result = 0
    if len(checking_no) <= 2:
        return result
    elif checking_no not in prize_list.keys():
        result+=check_result(prize_list, checking_no[1:])
    else:
        result = prize_list[checking_no]
    return result
        
#prize_list = {'45698621': 10000000, '19614436': 2000000, '96182420': 200000, '47464012': 200000, '62781818': 200000, '6182420': 40000, '7464012': 40000, '2781818': 40000, '182420': 10000, '464012': 10000, '781818': 10000, '82420': 4000, '64012': 4000, '81818': 4000, '2420': 1000, '4012': 1000, '1818': 1000, '928': 200, '899': 200, '118': 200, '420': 200, '012': 200, '818': 200}
#checking_list = ['12342411','12342425']
prize_list = create_list()
invoices = input()
checking_list = []
for i in range(int(invoices)):
    checking_list.append(input())

total_prize = 0

for i in checking_list:
    total_prize += check_result(prize_list, i)
print(total_prize)