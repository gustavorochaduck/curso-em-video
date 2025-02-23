print('-=-'*5)
print('10 TERMOS DE UMA PROGRECAO ARITIMETICA (PA)')
print('-=-'*5)

FirstTerm = int(input('Primeiro Termo: '))
rz = int(input('Razao: '))

some = 0
for x in range(FirstTerm, FirstTerm+10):
    if some >= 0:
        print(f'{FirstTerm + some} -->')
    else:
        print(f'{FirstTerm + some} -->')
    some += rz
