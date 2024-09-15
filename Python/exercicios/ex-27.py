name = str(input('Type your Name: ')).strip()
name_list = name.split()
print(f'The first Name is: {name_list[0]}')
def lastname():
    le = len(name_list)-1
    print('The Last name is: {}'.format(name_list[le]))

lastname()
#print(f'The Last name is: {n}')