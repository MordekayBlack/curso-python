# Crie um programa que escreva na tela Ola Mundo!

print('Ola Mundo!!!')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
soma = n1 + n2

#primeira forma de print
print('\n#Primeira forma de print')
print('A soma entre ',n1,' e ', n2 ,'= ',soma)

# Segunda forma de print
print('\n#Segunda forma de print')
print('A soma entre {} e {} = {}'.format(n1,n2,soma))

#Terceira  forma de print e a mais atual e a mais ultilizada
print('\n#Terceira  forma de print e a mais atual e a mais ultilizada')
print(f'A soma entre {n1} e {n2} = {soma}')