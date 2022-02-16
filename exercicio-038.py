'''  Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
    O primeiro valor é maior
    O segundo valor é maior
    Nao existe numero maior,os dois sao iguais'''

n1 = int(input('Digite o primeiro numero inteiro >> '))
n2 = int(input('Digite o segundo numero inteiro >> '))

if n1 == n2:
    print(f'O numero {n1} é igual ao numero {n2}')
elif n1 > n2:
    print(f'O numero {n1} é maior que o numero {n2}')
else:
    print(f'O numero {n2} é maior que o numero {n1}')