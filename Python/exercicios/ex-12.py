# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com um desconto de 5%
#2,29
import math
desconto = 5
print('Para selecionar os produdos digite os numeros!!!')
print('Coca-Cola: [1]')
print('Farinha-de-Trigo: [2]')
print('Leite: [3]')
print('Ovos: [4]')
print('Fermento: [5]')
print('Margarina: [6]')
print('Exit: [0]')
escolha01 = str(input('Digite o Numero do Produto: '))

if escolha01 =='0':
    input('')
elif escolha01 =='1':
    valor01 = 2.29
    desconto1 = valor01 * (desconto / 100)
    print(f'Valor da Coca-Cola sem desconto: R${valor01}')
    print(f'Valor da Coca-Cola com o desconto: R${desconto1}')
    input('')
elif escolha01 =='2':
    valor02 = 3.00
    desconto2 = valor02 * (desconto / 100)
    print(f'Valor da Farinha de Trigo sem o desconto: R${valor02}')
    print(f'Valor da Farinha de Trigo com desconto: R${desconto2}')
    input('')
elif escolha01 =='3':
    valor03 = 3.50
    desconto3 = valor03 * (desconto / 100)
    print(f'Valor do Leite sem desconto: R${valor03}')
    print(f'Valor do Leite com o Desconto: R${desconto3}')
    input('')
elif escolha01 =='4':
    valor04 = 10.40
    desconto4 = valor04 * (desconto / 100)
    print(f'Valor dos Ovos sem Desconto: R${valor04}')
    print(f'valor dos Ovos com Desconto: R${desconto4}')
    input('')
elif escolha01 =='5':
    valor05 = 3.25
    desconto5 = valor05 * (desconto / 100)
    print(f'Valor do Fermento sem o desconto: R${valor05}')
    print(f'Valor do Fermento com o desconto: R${desconto5}')
    input('')
elif escolha01 =='6':
    valor06 = 5.90
    desconto6 = valor06 * (desconto / 100)
    novo6 = valor06 - desconto6
    print(f'Valor da Margarina sem Desconto: R${valor06}')
    print(f'Valor da Margarina com Desconto: R${desconto6}')
    input('')
else:
    print('VOCE DIGITOU ALGO ERRADO!!!')
    input('')