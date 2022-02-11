# Crie um programa que leia um nome de uma cidade e mostre na tela se ela começa ou nao com 'Santo'

cidade = str(input('Digite o nome da cidade >> ')).title().strip()

# Primeira forma
print(cidade[:5] == 'Santo')

result = cidade.find('Santo')
if result == -1:
    print('Sua cidade nao começa com "Santo"')
else:
    print('Sua cidade começa com "Santo"')