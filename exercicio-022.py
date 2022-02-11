# Crie um program que leia um nome completo de uma pessoa e mostre o nome com toda as letras em maiuscula,o nome com todas as letras em minuscula,
# quantas letras tem   o nome sem considerar espaços,quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo >> ')).strip()
print(f'\nSeu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print(f'Seu nome Com a primeira letra em Maiscula: {nome.capitalize()}')
print(f'Seu nome com a primeira letra de cada nome em Maiuscula: {nome.title()}\n')

#tirando os espaços em branco c/ o split e o join
n = nome.split()
n1 = ''.join(n)
print(f'Seu primeiro nome é {n[0].title()} e ele comtem {len(n[0])} letras')
print(f'O tatal de caracteres considerando os espaços foi:{len(nome)}')
print(f'O tatal de caracteres do seu nome desconsiderando os espaços foi: {len(n1)}')
