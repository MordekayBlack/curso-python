# Escreva um programa que pergunte o salario de um funcionario e caucule seu aumento,para salario superior a R$1.250,00 caucule um aumento de 10%,
#     para salario inferior caucule um aumento de 15%

salario = float(input('Digite o salario do funcionário >> '))

ajuste10 = salario + (salario * 10 / 100)
ajuste15 = salario + (salario * 15 / 100)

if salario < 1250.00:
    salarioNovo = ajuste10
else:
    salarioNovo = ajuste15

print(f'Seu salário anterior era R${salario} reais, como o novo reajuste passará a receber R${salarioNovo} reais')