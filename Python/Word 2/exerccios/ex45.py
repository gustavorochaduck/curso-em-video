import random
from time import sleep

attacks_list = ['papel', 'pedra', 'tesoura']

# pe = 'pedra'
# pa = 'papel'
# te = 'tesoura'

print('Pedra')
print('Papel')
print('Tesoura')
print('---' * 20)
user_attack = str(input('Select: ').lower())
print('---' * 20)
print('Se prepare!!!')


def random_attack(attack_list, user_attack):
    if user_attack in attack_list:
        attacks_list.remove(user_attack)
    if attacks_list:
        at = random.choice(attacks_list)
    else:
        at = None
    return at

selected_attack = random_attack(attacks_list, user_attack)

sleep(0.5)
print('1')
sleep(1)
print('2')
sleep(1)
print('3')
sleep(1)
print('JA !!!')
print('---' * 20)
print('User - {}'.format(user_attack))
print('Computer - {}'.format(random_attack()))

if user_attack == 'pedra' and random_attack() == 'tesoura':
    print('---' * 20)
    print(f'Voce ganhou!!!')
elif user_attack == 'tesoura' and random_attack() == 'pedra':
    print('---' * 20)
    print('Computador ganhou!!!')
elif user_attack == 'tesoura' and random_attack() == 'papel':
    print('---' * 20)
    print('Voce ganhou!!!')
elif user_attack == 'papel' and random_attack() == 'tesoura':
    print('---' * 20)
    print('Computador Ganhou!!!')
elif user_attack == 'pedra' and random_attack() == 'papel':
    print('---' * 20)
    print('Computador Ganhou!!!')
elif user_attack == 'tesoura' and random_attack() == 'pedra':
    print('---' * 20)
    print('Computador ganhou!!!')
