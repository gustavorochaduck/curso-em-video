import random
import os
import sys

selectet_number = int(input('Select a number (0-10): ').strip())


def rando_mnumber():
    number_list = list(range(11))
    random_number = random.choice(number_list)
    return random_number

def restart():
    restart_answer = str(input('You want to Restart the Program? (Y/N): ').strip().lower())

    if restart_answer == 'n' or restart_answer == 'not':
        print('Goodbye!!!')
    elif restart_answer == 'y' or restart_answer == 'yes':
        os.execv(sys.executable, ['python'] + sys.argv)


if selectet_number == rando_mnumber():
    print('You selectet the rigth one!!!')
    print(f'What your typed: {selectet_number}')
    print(f'The Random number: {rando_mnumber()}')
elif selectet_number < rando_mnumber():
    print('You are unlucky!!!')
    print(f'Wath you typed: {selectet_number}')
    print(f'The random number was: {rando_mnumber()}')

elif selectet_number > rando_mnumber():
    print('You are unlucky!!!')
    print(f'Wath you typed: {selectet_number}')
    print(f'The random number was: {rando_mnumber()}')
else:
    print('You typed somthing rong')
    print(selectet_number)
    restart()
    
restart()
