# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados EX: 8945 milhar:8 centena:9 dezena:4 unidade:5

n = int(input('Digite um numero com quatro digitos entre 0 e 9999 >> '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Milhares: {m}')
print(f'Centenas: {c}')
print(f'Dezenas: {d}')
print(f'Unidades: {u}')