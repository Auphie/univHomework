def find_bmi(weight, hight):
    bmi = weight/hight**2
    if weight < 20 or weight > 300:
        print('Input Error 20~300')
    elif hight < 0.5 or hight > 2.5:
        print('Input Error 0.5~2.50')
    elif bmi < 18.5:
        print("BMI too low")
    elif bmi > 24:
        print("BMI too hight")
    else:
        print('%.2f'%bmi)   

while True:
    inputs = input()
    if inputs == '-1':
        break
    else:
        weight=float(inputs.split(' ')[1])
        hight=float(inputs.split(' ')[0])
        find_bmi(weight,hight)
