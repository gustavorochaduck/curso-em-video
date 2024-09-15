km_desejado = float(input('Quantos quilometros voce deseja viajar?: ').strip())
primeiro_valor = 0.50
segunbdo_valor = 0.45
# viagens de acima de 200km
km = 200


def calculo_perto():
    valor_total_perto = km_desejado * primeiro_valor
    return valor_total_perto


def calculo_longe():
    valor_total_longe = km_desejado * segunbdo_valor
    return valor_total_longe


if km_desejado <= 200:
    print(f'O valor da passagem vai ser de: R${calculo_perto()}')
elif km_desejado > km:
    print(f'O valor da passagem vai ser de: R${calculo_longe()}')
