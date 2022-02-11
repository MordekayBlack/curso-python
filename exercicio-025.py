# Crie um programa que leia um nome de uma pessoa e diga se ela posue 'Silva' no nome

nome = str(input('Digite o nome completo >> ')).strip().title()
print('Seu nome tem Silva:','Silva' in nome)