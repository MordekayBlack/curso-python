nome = str(input('Digite seu nome >> ')).strip().title()
if nome == 'Leonardo':
    print(f'Bonito seu nome!{nome}.')

elif nome == 'Lavinya' or nome == 'Marlene':
    print(f'Adorei seu nome {nome}')

elif nome in 'Daniel Danilo':
    print(f'Seu nome é de viado {nome}')
else:
    print(f'Seu nome é comum.')
print(f'Tenha um bom dia {nome}!')
