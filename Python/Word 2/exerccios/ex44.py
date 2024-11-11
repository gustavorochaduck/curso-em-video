product_value = float(input('Valor da compra: '))
print('---' * 20)
print('Tipos de Pagamento:')
print('a vista em dinheiro - 10% de desconto')
print('a vista com cartao - 5% de desconto')
print('2x no cartao - valor completo')
print('3x ou mais no cartao - 20% de juros')
print('---' * 20)
print('A vista com Dinheiro - [1]')
print('A vista com cartao - [2]')
print('2x no cartao - [3]')
print('3x ou mais no cartao - [4]')
print('---' * 20)
select = int(input('select: '))


def vista_dinheiro():
    a = product_value - ((10 * product_value) / 100)
    return a


def vista_cartao():
    b = product_value - ((5 * product_value) / 100)
    return b


def cartao2():
    return product_value


def cartao3():
    c = ((20 * product_value) / 100) + product_value
    return c


if select == 1:
    print('---' * 20)
    print('Valor da Compra: R${:.2f}'.format(vista_dinheiro()))
    print('---' * 20)
elif select == 2:
    print('---' * 20)
    print('Valor da Compra: R${:.2f}'.format(vista_cartao()))
    print('---' * 20)
elif select == 3:
    print('---' * 20)
    print('Valor da Compra: R${:.2f}'.format(cartao2()))
elif select == 4:
    print('---' * 20)
    print('Valor da Compra: R${:.2f}'.format(cartao3()))
input('')
