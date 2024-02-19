#Crie um algoritimo que le um numero e mostre o seu dobro e a sua raiz quadrada
#EU SO SEI FAZER A RAIZ QUADRADA COM A BIBLIOTECA MATH

import math

valor = int(input('Digite um valor: '))

dobro = valor + valor
raiz = math.sqrt(valor)

print(f'Valor digitado: {valor}')
print(f'O Dobro: {dobro}')
print(f'A raiz: {raiz}')