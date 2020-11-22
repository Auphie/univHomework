import math
def find_bmi(name, hight, weight):
    bmi = weight/hight**2
    if bmi < 18.5:
        result = ' too LOW'
    elif bmi > 24:
        result = ' too HIGH'
    else:
        result = ''
    print('Hi %s, Your BMI: %f%s.'%(name, bmi, result))

name = input()
i_hight= float(input())
i_weight= float(input())
find_bmi(name, i_hight/100, i_weight)