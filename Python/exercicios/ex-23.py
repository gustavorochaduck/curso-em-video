num = int(input('Type one number (1 - 9999): '))

def unit():
    u = num // 1 % 10
    print(f'Unit: {u}')
def ten():
    t = num // 10 % 10
    print(f'Ten: {t}')
def hundred():
    h = num // 100 % 10
    print(f'Hundread: {h}')
def thousand():
    th = num // 1000 % 10
    print(f'Thousand: {th}')

print(f'Number: {num}')
unit()
ten()
hundred()
thousand()