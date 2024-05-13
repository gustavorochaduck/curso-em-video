import math

print('Celsius [1]')
print('Fahrenheit [2]')
value1 = int(input('Chose: '))

if value1 == 1:
    untransform1 = float(input('Celsius value: '))
    transform1 = (9/5*untransform1) + 32
    print(f'Celsius Value: {untransform1} °C')
    print(f'Fahrenheit value: {transform1} °F')
elif value1 == 2:
    untransform2 = float(input('Fahrenheit value: '))
    transform2 = (untransform2 - 32)*5/9
    print(f'Fahrenheit value: {untransform2} °F')
    print(f'Celsius value: {transform2} °C')
else:
    print('You typed something wrong!!!')