number = int(input('Type the number: '))

number_alone = number % 2

print(number_alone)
if number_alone >= 0:
    print(f'This number is Par: {number_alone}')
elif number_alone == 0:
    print(f'This Number is impar: {number_alone}')
else:
    print('You typed somthing wrong!!!')
