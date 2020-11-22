def find_bmi(weight, hight):
    bmi = weight/hight**2
    if weight < 20 or weight > 300:
        print('Input Error(20~300)')
    elif hight < 0.5 or hight > 2.5:
        print('Input Error(0.5~2.50)')
    elif bmi < 18.5:
        print("BMI too low (%s)"%bmi)
    elif bmi > 24:
        print("BMI too high (%s)"%bmi)
    else:
        print('BMI = %s'%bmi)   

while True:
    hight=float(input('hight = ? m'))
    if int(hight) == -1:
        break
    else:
        weight=float(input('weight = ? kg'))
    if int(weight) == -1:
        break
    else:
        find_bmi(weight,hight)
        continue