#exercicio 46: Faca um programa que mostra na tela uma contagem regressiva para o estouro de fogos de exervicios, indo de 0 a 10, com uma pausa de um segundo entre eles
import time

input('Clique a tecla [ENTER] para comecar a contagem: ')
print("-=-"*20)
for c in range(1, 10+1):
    print(c)
    time.sleep(1)
print("-=-"*20)