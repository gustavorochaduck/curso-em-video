import math

# Diario R$60
# kilometro R$0.15
day_price = 60.00
km_price = 0.15

print('Quando Dias?')
days = float(input(' '))
print('Quantos Quilometros?')
kms = float(input(' '))

cal1 = (days*day_price) + (kms*km_price)
print(f'O Custo ficou de: R${cal1}')