# Escreva um programa que leia a velocidade de um carro,se ele ultrapassar 80km ele sera multado,a multa sera de R$7,00 por cada km exedido

from random import randint

acelerar = randint(10,50)
vel = 60
velTotal = vel + acelerar
multa = float((velTotal - 80) * 7)
print('Velocidade Maxima da via 80km!')
if velTotal > 80:
    print(f'Sua velocidade atual é {velTotal}\nVocê acaba de receber uma multa.\nDiminua a velocidade!')
    print(f'O valor da multa é R${multa:.2f}')
else:
    print(f'Parabens!!Sua velocidade atual é {velTotal}.\nBoa viagem!!Dirija com segurança.')