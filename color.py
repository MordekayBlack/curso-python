import colorterminal
print('Ola \033[0;0;41mmundo\033[m')
print(f'Ola {colorterminal.ColorText.BLUE}mundo')

cores = {'limpa': '\033[m',
        'branca': '\033[30m',
        'azul' :'\033[34m',
        'amarelo' : '\033[33m',
        'pretoBranco' : '\033[7;30m'}
print(f'Ola{cores["amarelo"]} mundo{cores["limpa"]}')