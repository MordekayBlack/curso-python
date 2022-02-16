'''    A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria:
    Até 9 anos:mirim
    Até 14 anos infantil
    Até 19 anos junior
    até 20 anos senior
    acima de 20 anos master'''

from datetime import date

nasc = int(input('Digite o ano de nascimento >> '))
idade = date.today().year - nasc

if idade <= 9:
    print(f'A idade do atleta é \033[32m{idade}\033[m anos')
    print('De acordo com a idade do atleta, sua categoria sera \033[31mMIRIM')
elif idade > 9 and idade <= 14:
    print(f'A idade do atleta é \033[32m{idade}\033[m anos')
    print('De acordo com a idade do atleta, sua categoria sera \033[31mINFANTIL')
elif idade > 14 and idade <= 19:
    print(f'A idade do atleta é \033[32m{idade}\033[m anos')
    print('De acordo com a idade do atleta, sua categoria sera \033[31mJUNIOR')
elif idade > 19 and idade <= 20:
    print(f'A idade do atleta é \033[32m{idade}\033[m anos')
    print('De acordo com a idade do atleta, sua categoria sera \033[31mSENIOR')
else:
    print(f'A idade do atleta é \033[32m{idade}\033[m anos')
    print('De acordo com a idade do atleta, sua categoria sera \033[31mMASTER')