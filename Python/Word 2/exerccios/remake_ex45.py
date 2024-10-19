import random
from time import sleep

def decoration():
    decoration = print('---'*20) 
    return

def clock():
    sleep(1)
    s1 = print('1')
    sleep(1)
    s2 = print('2')
    sleep(1)
    s3 = print('3')
    sleep(1)
    go = print('JÁ')


#list of attacks
attack = ["pedra", "papel", "tesoura"]

#the game
print('Selecione um Ataque:')
for x in attack:
    print(x)
sleep(0.5)
decoration()
user_attack = str(input('Ataque: '))
sleep(0.5)
print(f"Ataque selecionado: {user_attack.lower}")
decoration()

attack.remove(user_attack)
ran = random.choice(attack)

clock()
decoration()
sleep(0.5)
print(f"Jogador: {user_attack}")
sleep(0.5)
print(f"Computer: {ran}")
decoration()

if user_attack == "papel" and ran == "pedra":
    sleep(0.5)
    print("Você Ganhou da Maquina!!!")
    sleep(0.5)
    print("Parabéns!!!")
elif user_attack == "pedra" and ran == "tesoura":
    sleep(0.5)
    print("Você Ganhou da Maquina!!!")
    sleep(0.5)
    print("Parabéns!!!")
elif user_attack == "tesoura" and ran == "papel":
    sleep(0.5)
    print("Você Ganhou da Maquina!!!")
    sleep(0.5)
    print("Parabéns!!!")
else:
    sleep(0.5)
    print("Você perdeu o Jogo :( ")
    sleep(0.5)
    print("Tente Novamente!!!")

decoration()
sleep(0.5)
print("Feito por GUSTAVO ROCHA DÜCK")
sleep(0.5)
input("Digite Qualquer tecla para SAIR!!!: ")