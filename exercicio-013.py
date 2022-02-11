# Faça um programa que leia um salario de um funcionaio e mostre o valor do novo salario com aumento de 15%

salario = float(input('Digite seu salario atual >>R$  '))
ajuste = int(input('Digite o o percetual do reajuste(%) >> '))

ajusteSalario = salario + (salario * ajuste / 100)

print(f'Seu salario ataul é {salario:.2f}, com o reajuste de {ajuste}% , passara a ser de R${ajusteSalario:.2f}')