import math

print('Cateto - Cateto [1]')
print('Cateto - Hipotenusa [2]')
chose = int(input('Select: '))

if chose == 1:
    value1 = float(input('Cateto 1: '))
    value2 = float(input('Cateto 2: '))

    call1 = round(math.sqrt(value1**2 + value2**2),2)

    print(f'Valor da Hipotenusa é: {call1}')
elif chose == 2:
    value01 = float(input('Cateto: '))
    value02 = float(input('Hipotenusa: '))
    
    call2 = round(math.sqrt(value02**2 - value01**2),2)

    print(f'Cateto é: {call2}')
