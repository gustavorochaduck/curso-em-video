#Crie uma carteira que ele pode comprar dollar
#Tem o modo normal e o mais avancado
import math

dollar = 4.46
wallet = float(input('A quantidade de dinheiro que tem a sua Cartira: '))
escolha1 = str(input('Digite S para simples, e A para avancado: '))

if escolha1 =='s':
    if wallet >= dollar:
        compra = wallet / dollar
        print(f'Voce consegue compar ${compra} dolare')
        escolha2 = str(input('Voce ira comprar? Se sim digite y . Para nao n: '))
        if escolha2 =='y':
            print(f'Compra de ${compra} Confirmada!!!')
        elif escolha2 =='n':
            print('Compra Cancelada...')
        else:
            print('Voce Digitou algo de errado!!!')
    elif wallet <= dollar:
        print('Valor da Carteira muito Baixa')
        print('Nao tem como fazer uma compra')
    else:
        print('Voce digitou algo errado!!!')
