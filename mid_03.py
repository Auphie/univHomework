def checkBmi(hight, weight):
    bmi = weight/hight**2
    if (hight < 0.5 or hight > 2.5):
        print('Input Error 0.5~2.50')
    elif (weight < 20 or weight > 300):
        print('Input Error 20~300')
    elif bmi > 24:
        print('BMI too high')
    elif bmi < 18.5:
        print('BMI too low')
    else:
        print('%.2f'%bmi)    

def main():
    while True:
        inputs = input().split()
#        inputs = ['3', '20']
        if inputs[0] != '-1':
            hight = float(inputs[0])
            weight = float(inputs[1])
            checkBmi(hight, weight)
        else:
            break
main()