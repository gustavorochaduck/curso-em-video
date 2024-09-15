import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista_de_alunos01 = [n1, n2, n3, n4]
random.shuffle(lista_de_alunos01)
print(lista_de_alunos01)