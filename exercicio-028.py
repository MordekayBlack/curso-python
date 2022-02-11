#Escreva um programa que faça o computdor pensar,em um numero inteiro entre 0 a 5, e peça o usuario tentar adivinhar qual foi o
# numero escolhido pelo computador  O programa deve escrever na tela se o usuario venceu ou perdeu

from random import randint
n = randint(1,5)
print('Tente adivinhar qual numero a maquina penssou!Boa sorte!!')
n2 = int(input('Digite um numero >>  '))
if n == n2:
    print(f'A maquina escolheu {n} e você escolheu {n2}')
    print('Parabens!!Você acertou')
else:
    print(f'A maquina escolheu {n} e você escolheu {n2}')
    print('Tente novamente,voce errou :(')
