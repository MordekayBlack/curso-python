'''O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de um trabalho dos alunos,
    faça um programa que leia o nome dos quatros alunos e mostre a ordem que os alunos iram apresentar os trabalhos.'''

from random import shuffle
a1 = str(input('Digite o nome do 1° aluno >> ')).strip().capitalize()
a2 = str(input('Digite o nome do 2° aluno >> ')).strip().capitalize()
a3 = str(input('Digite o nome do 3° aluno >> ')).strip().capitalize()
a4 = str(input('Digite o nome do 4° aluno >> ')).strip().capitalize()

alunos = [a1,a2,a3,a4]

print('A ordem sorteado para a apresentação foi:')
print(f'{shuffle(alunos)}')
print(alunos)