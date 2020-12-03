c = 1
while c<=100:

    x = float(input('your height in meters: '))
    y = float(input('enter your weight in Kg: '))

    z = y/ x ** 2

    print(z)

    if z >= 25:
        print('you are over weight,please consult a docter')

    elif z <= 18:
        print('you are underweight,just eat more ;)')

    else:
        print('you are healthy')

    print('')

    c=c+1