# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# E a quantidade de tinta necessário para pinta-la. sabendo que cada litro de tinta, pinta uma
# Área de 2 metros quadrados

import math

a = float(input('Altura: '))
l = float(input('Largura: '))
tinta = 2

area = a*l
qunatidade = area // tinta

print(f'Area para ser pintada: {area}')
print(f'Quantos Baldes de Tintas: {qunatidade}')