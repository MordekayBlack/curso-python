#Faça um programa que leia um numero inteiro qualquer e mostre sua taboda

#este exercicio era para fazer sem o uso do for mas achei desnescessario

print(f'{" Tabuada ":=^50}')
v = int(input('Digite um numero >> '))
for n in range(0,11):
    print(f'{v} X {n} = {v * n }')

