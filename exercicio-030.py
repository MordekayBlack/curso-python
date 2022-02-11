# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

n = int(input('Digite um numero >> '))
if n % 2 == 0:
    print(f'O numero {n} é par')
else:
    print(f'O numero {n} é impar')