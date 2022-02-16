# Desenvolva um programa que leia 6 numeros inteiros e mostre a soma somete daqueles que forem pares,se o valor digitado for impar desconsidere
soma = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° numero >> '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos numeros pares foi {soma}')