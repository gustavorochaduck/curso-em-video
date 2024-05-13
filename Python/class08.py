import math

num = int(input('Digite qualquer numero: '))
raiz = math.sqrt(num)
arendondamento = math.ceil(raiz)
print(f'A raiz de {num} é {arendondamento}')