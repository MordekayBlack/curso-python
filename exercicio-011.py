'''Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua area e a quantidade de
    tinta nescessaria para pintar a parede ,sabendo que cada litro de tinta pinta uma area de 2m²'''

l = float(input('Digite a largura da parede em Metros >> '))
a = float(input('Digite a altura da perede em Metros>> '))

totArea = l * a
tinta = totArea / 2
print(f'O total da area calculada de toda parede = { totArea } m²')
print(f'Para pintar a parede você ira gastar {tinta} litros de tintas')