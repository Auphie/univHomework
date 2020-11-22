def input_schedule():
    code = int(input())
    hour = int(input())   
    schedules = [code, hour]
    for i in range(hour):
        schedules.append(int(input()))
    return schedules

def check_conflict(*schedule):
    for pair in range(0, len(schedule)-1):  # set length of pairs to pinch (classes -1)
        for i in schedule[pair][2:]:        # take target period from L to R to do pinch match
            for j in range(pair+1, len(schedule)):  # j is index of classes to do pair comparison
                if i in schedule[j][2:]:    # check i is in schedule[j]
                    print('{0} and {1} confict on {2}'.format(schedule[pair][0],
                        schedule[j][0], i))
                    continue

sch_1 = input_schedule()
sch_2 = input_schedule()
sch_3 = input_schedule()
check_conflict(sch_1, sch_2, sch_3)
#check_conflict([1001, 3, 11, 12, 13], [1002, 3, 21, 22, 23],
#[1003, 3, 31, 32, 13],[1004, 3, 41, 22, 43])