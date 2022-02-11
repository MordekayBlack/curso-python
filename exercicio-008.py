# crie um programa que leia um valor em metros e mostre o resultado convertido em centimetros e em milemetros

v = float(input('Digite um valor em METROS >> '))
cm = v * 100
ml = v * 1000

print(f'{v} metros convertido em centimetro {cm:.0f}Cm \n{v} metros convertido em milemetros = {ml:.0f}mm')