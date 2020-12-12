c = 0
while c < 1:

    x = float(input('Your height in meters:- '))
    y = float(input('Enter your weight in Kg:- '))

    z = y/ x ** 2

    print('Your BMI is: {:1.2f}'.format(z))

    if z >= 25:
        print('You are over weight,please consult a doctor')

    elif z <= 18:
        print('You are underweight,please consult a doctor')

    else:
        print('You are healthy')

    print('')

    
