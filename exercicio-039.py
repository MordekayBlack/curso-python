'''  Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
    Se ele ainda vai se alistar ao serviço militar.
    Se é a hora de se alistar
    Se ja passou o tempo de listamento
    O seu programa tambem deve mostrar o tempo que falta, ou o tempo que passou do prazo.'''

from datetime import date

nasc = int(input('Digite o ano que você nasceu >> '))
idade = date.today().year - nasc

if idade < 18:
    dif = 18 - idade
    print('Fique tranquilo ainda não é a hora de você se alistar')
    print(f'Falta {dif} anos.')

elif idade == 18:
    print('Parabens!!Você esta na idade ideal para se alistar.')
    print('Procure uma unidade da \033[32mMarinha\033[m,\033[32mAeronautica\033[m ou \033[32mExercito Brasilerio\033[m e realise seu alistamneto.')
elif idade > 18:
    dif = idade - 18
    print(f'Ops!Você esta em atraso com suas obrigaçoes militares a {dif} anos.')
    print(f'Procure uma unidade da \033[32mMarinha\033[m , \033[32mAeronautica\033[m ou \033[32mExercito Brasilerio\033[m e regularize sua situação.')