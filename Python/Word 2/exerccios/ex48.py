#Exercicio 48: faca um programa que calcule a soma entre todos os numeros impareres que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
some = 0
cont = 0 
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        #print(c, end=" ")
        some = some + c
        cont = cont + 1

print(f'The same of {cont} | values solicitated are: {some}')