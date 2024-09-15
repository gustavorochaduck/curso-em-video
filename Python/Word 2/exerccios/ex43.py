peso = float(input('Digite o seu peso em Quilos: '))
altura = float(input('Digite a sual altura em metros: '))


def imc():
    a = peso / (altura ** 2)
    return a


if imc() < 18.5:
    print('---' * 20)
    print('{:.2f}kg - esta abaixo do peso!!!'.format(imc()))
    print('---' * 20)
elif imc() == 18.5 or imc() < 25:
    print('---' * 20)
    print('{:.2f}kg - esta no peso ideal'.format(imc()))
    print('---' * 20)
elif imc() == 25 or imc() < 30:
    print('---' * 20)
    print('{:.2f}kg - esta com sombre peso!'.format(imc()))
    print('---' * 20)
elif imc() == 30 or imc() < 40:
    print('---' * 20)
    print('{:.2f}kg - Esta com Obesidade!!'.format(imc()))
    print('---' * 20)
elif imc() >= 40:
    print('---' * 20)
    print('{:.2f} - Obesidade MORBIDA!!!'.format(imc()))
    print('---' * 20)
else:
    print('ERROR!!!')
input()
