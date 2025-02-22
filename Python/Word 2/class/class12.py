name = str(input('Whats is your name?: ').strip())
name_list = ['pedro', 'maria', 'john']

if name.lower() == 'gustavo':
    print('Your name is Beautiful {}'.format(name))

elif name.lower() in name_list:
    print('{} is a popular name'.format(name))

else:
    print('{} is a normal Name'.format(name))
    
print('Welcome {}'.format(name))
