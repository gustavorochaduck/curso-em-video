reta01 = float(input('Digite a primeira Reta: '))
reta02 = float(input('Digite a segunda Reta: '))
reta03 = float(input('Digite a Terceira Reta: '))

if reta01 + reta02 > reta03 and reta01 + reta03 > reta02 and reta02 + reta03 > reta01:
    print('Essa medida é compativel com um triangulo!')
else:
    print('Essa medida não é compativel com um Triangulo')