salario = float(input('Qual é o valor do seu Salario: R$'))


def calculo1():
    resultado1 = (salario * 15 / 100) + salario
    return resultado1

def calculo2():
    resultado2 = (salario * 10 / 100) + salario
    return resultado2

if salario <= 1200.00:
    print(calculo1())
elif salario > 1200.00:
    print(calculo2())