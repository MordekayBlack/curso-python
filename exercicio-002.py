# Faça um programa que leia um nome de uma pessoa e mostre uma mensagem de boas vindas

nome = input('Digite seu nome :> ').strip()
print(f'Seja bem vindo! {nome}.\n')

n1 = bool(input('digite um numero: '))
print(n1,'\n')

#verifica se é numero

var1 = input('Digite algo: ')
if var1.isnumeric():
    print('Foi digitado um numero')
elif var1.islower():
    print('Foi digitado tudo em minusculo')