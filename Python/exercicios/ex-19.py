import random

print('Type only 4 names:')
al1 = str(input('Name 1: '))
al2 = str(input('Name 2: '))
al3 = str(input('Name 3: '))
al4 = str(input('Name 4: '))
lists = (al1, al2, al3, al4)
ra = random.choice(lists)

print(f'The choice is: {ra}')