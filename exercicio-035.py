#Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou nao formar um triagulo

r1 = int(input('Digite o comprimento da primera reta de um triangulo >> '))
r2 = int(input('Digite o comprimento da segunda reta de um triangulo >> '))
r3 = int(input('Digite o comprimento da terceira reta de um triangulo >> '))

if (r1 + r2) < r3:
    print('O valor das tres retas forma um triangulo.')
if (r1 + r3 ) < r2:
    print('O valor das tres retas forma um triangulo.')
if (r2 + r3 ) < r1:
    print('O valor das tres retas forma um triangulo.')
else:
    print('O valor das tres retas nao  forma um triangulo.')