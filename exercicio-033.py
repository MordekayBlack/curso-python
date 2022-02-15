#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro numero >> '))
n2 = int(input('Digite o segundo numero >> '))
n3 = int(input('Digite o terceiro numero >> '))

menor = n1
maior = n1

if n1 < n2  and n1 < n3 :
    menor = n1

elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor numero é {menor}\nO maior numero é {maior}')
