import datetime

name = input('Digite o seu nome para o alistamento: ').strip()
client_year = int(input('Digite o ano do seu nascimento: '))


def current_year():
    return datetime.date.today().year


age = current_year() - client_year
required_age = 18

if age == required_age:
    print('-=-' * 20)
    print(f'Você, {name.upper()}, está pronto para servir!!!')
    print('-=-' * 20)
elif age < required_age:
    print('-=-' * 20)
    print(f'{name.upper()}, você ainda não pode se alistar por ser menor de idade!')
    print(f'Ainda faltam {required_age - age} anos.')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print(f'Já se passaram {age - required_age} anos do seu prazo de alistamento!')
    print('Você terá que pagar uma MULTA ou conversar com um responsável pelo alistamento!')
    print('-=-' * 20)

input('')
