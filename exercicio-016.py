# Faça um programa que leia um numero real e mostre na tela sua porção inteira

from math import trunc
n1 = float(input('Digite um numero decimal >> '))
print(f'O numero digitado foi {n1}, e sua parte inteira é {n1:.0f}\n')

n2 = float(input('Digite outro numero decimal >> '))
print(f'O numero digitado foi {n2},a sua parte inteira é {trunc(n2)}\n')

n3 = float(input('Digite outro numero decimal >> '))
print(f'O numero digitado foi {n2},a sua parte inteira é {trunc(n2)}\n')

n4 = float(input('Digite um valor decimal >>'))
print(f'O valor digitado foi {n4} e sua porção inteira é {int(n4)}')