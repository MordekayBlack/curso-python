# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

v = float(input('Digite o valor do produto >>R$ '))
desc = int(input('Digite o valor do desconto(%) >> '))

valDesc = v - (v * desc / 100)
print(f'O valor inicial do produto = R${v} ,com o desconto de {desc}% o produto passara a custar R${valDesc}')