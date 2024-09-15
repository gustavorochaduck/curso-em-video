reta01 = float(input('Digite a primeira Reta: '))
reta02 = float(input('Digite a segunda Reta: '))
reta03 = float(input('Digite a Terceira Reta: '))

if reta01 + reta02 > reta03 and reta01 + reta03 > reta02 and reta02 + reta03 > reta01:
    print('---' * 20)
    print('Essa medida é compativel com um triangulo!')
    print('---' * 20)
    if reta01 == reta02 and reta01 == reta03:
        print('---' * 20)
        print('Esse triangulo e um Equilatero ')
        print('---' * 20)
    elif reta01 == reta02 or reta03 == reta02:
        print('---' * 20)
        print('Esse triangulo e um Isoseles')
        print('---' * 20)
    else:
        print('---' * 20)
        print('Esse triangulo e Escaleno')
        print('---' * 20)
else:
    print('Essa medida não é compativel com um Triangulo')