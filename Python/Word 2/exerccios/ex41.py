from time import sleep
import datetime
name = str(input('Digite o seu nome: ').strip().lower())
client_age_date = int(input('Digite a data do seu nacimento: '))
today = datetime.date.today().year
client_age = today - client_age_date

if client_age < 9:
    print('-=-' * 20)
    print(f'{name.upper()} foi calsificado como MIRIM')
    print('-=-' * 20)
elif client_age == 9 or client_age < 14:
    print('-=-' * 20)
    print(f'{name.upper()} foi clasificado como INFANTIL')
    print('-=-' * 20)
elif client_age == 14 or client_age < 19:
    print('-=-' * 20)
    print(f'{name.upper()} foi clasificado como JUNIOR')
    print('-=-' * 20)
elif client_age == 19 or client_age < 20:
    print('-=-' * 20)
    print(f'{name.upper()} foi clasificado como SENIOR')
    print('-=-' * 20)
elif client_age >= 20:
    print('-=-' * 20)
    print(f'{name.upper()} foi clasificado como MASTER')
else:
    print('you typed somthing wrong!!!')
input('')
