# Faça um programa que leia um ano qualquer e fale se ele é bissexto
from datetime import date
print('-=-'*30,f'\n{"ano bissexto":^90}','\n','-=-'*30)
ano = int(input('Digite o ano que deseja analizar >> '))

# o ano tem que ser divisivel por 4
# mesmo sendo divisivel por 4 ele nao porde ser divisivel por 100
# tem que ser divisivel por 100 e por 400
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto.')