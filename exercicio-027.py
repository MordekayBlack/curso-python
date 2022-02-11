# programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e ultimo nome separadamente EX: Primeiro: Leonardo Ultimo: Oliveira

nome = input('Digite seu nome completo >> ').strip().title()
pn = nome.find(' ')
un = nome.rfind(' ')


print(f'Seu primeiro nome é : {nome[:pn]}')
print(f'Seu ultimo nome é : {nome[un:]}\n')

#outra forma
print('Segunda forma de realizar o exercicio')
nomeS = nome.split()
print(f'Seu primeiro nome é :{nomeS[0]}')
print(f'Seu ultimo nome é : {nomeS[len(nomeS)-1]}')