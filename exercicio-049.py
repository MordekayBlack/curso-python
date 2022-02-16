#Refaça o exercicio 09 mostrando a taboada de um numero que o usuario escolher,so que agora ultilizando o for

print(f'{" Tabuada ":=^30}')
n = int(input('Digite o numero >> '))
for c in range(1,11):
    print(f'{n} X {c} = {n*c}')