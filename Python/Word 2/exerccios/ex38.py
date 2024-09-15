number1 = int(input('Type a number: '))
number2 = int(input('Type the second number: '))

if number1 > number2:
    print('-=-'*20)
    print(f'Number {number1} is Bigger as number {number2}')
    print('-=-' * 20)
elif number1 < number2:
    print('-=-' * 20)
    print(f'Number {number2} is Bigger as number {number1}')
    print('-=-' * 20)
elif number1 == number2:
    print('-=-' * 20)
    print(f'Number {number1} is equal as number {number2}')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('You typed somthing wrong !!!')
    print('-=-' * 20)
input('')