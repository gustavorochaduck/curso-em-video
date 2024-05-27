import random
escolha01 = int(input('Digite [1] para numeros e [2] para Palavras'))


if escolha01 ==1:
    escolha02 = int(print('Difite A Quantidade de Objetos que serão Sorteados [2-20]:'))
    if escolha02 ==2:
        quantidade_inicio = str(input('Numero Inicial: '))
        quantidade_terminio = str(input('Numero de Terminio: '))
        cal01 = quantidade_inicio - quantidade_terminio
        list02 = 'dfgb'
        al1_0 = random.choice