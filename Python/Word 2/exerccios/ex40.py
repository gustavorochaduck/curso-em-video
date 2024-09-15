nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))


def media():
    a = (nota1 + nota2) / 2
    return a


if media() < 5:
    print('-=-'*20)
    print('VOCÇÊ FOI REPROVADO!!!')
    print(f'A sua Média foi: {media()}')
    print('-=-' * 20)
elif media() == 5 or media() == 6:
    print('-=-' * 20)
    print('Você está de Recuperação!!!')
    print(f'A sua média foi: {media()}')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Aprovado!!!')
    print(f'Média: {media()}')
    print('-=-' * 20)
