# crie um programa que leia quantos ele tem na carteira e mostre quantos dolares ele pode comprar 1dolar=3,27

valor = float(input('Digite o valor que você possue na carteira >>R$ '))
dolar = valor / 3.27

print(f'Com este valor R${valor:.2f}, voce consegue compra USD {dolar:.2f} dolar ')