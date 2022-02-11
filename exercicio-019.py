#Um professor quer sortear um dos seus quatros alunos para apagar o quadro,faça um programa que ajude ele,leia o nome desses
#   quatros alunos e mostre na tela o nome do escolhido aleatoriamente
from random import choice
a1 = str(input('Digite o nome do 1° aluno >> ')).strip().capitalize()
a2 = str(input('Digite o nome do 2° aluno >> ')).strip().capitalize()
a3 = str(input('Digite o nome do 3° aluno >> ')).strip().capitalize()
a4 = str(input('Digite o nome do 4° aluno >> ')).strip().capitalize()
alunos = [a1,a2,a3,a4]

print(f'O aluno sortedo para apagar o quadro foi {choice(alunos)}!')