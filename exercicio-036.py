''' Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.O programa vai perguntar o valor da casa,
    o salario do comprador e em quantos anos ele vai pagar.Calcule o valor da prestação mensal sabendo que ela nao pode exeder 30% do salario,ou entao
    o emprestimo sera negado.'''

from datetime import date
vImovel = float(input('Digite o valor do imovel que deseja adquirir >>R$ '))
vSalario = float(input('Digite o valor do seu salario >>R$ '))
Qano = int(input('Em quantos anos deseja realizar o pagamento? >> '))

Qparc = Qano * 12 # quantidade de parcela
vMaxParc = vSalario * 30 / 100 # calcula 30% do salario
vParc = vImovel / Qparc # valor da parcela

#Calcula quantidade minima de parcela
QMimParc = 1
vMinParc = float(0) # valor minimo da parcela
while True:
    vMinParc = vImovel / QMimParc
    if vMinParc > vMaxParc:
        QMimParc += 1
    else:
        break

qMinAno = QMimParc // 12 # pega a quantidade minima de anos referente aos 30% do salario
print(f'\n{" Resultado da analise de credito ":=^50}')
if vParc > vMaxParc:
    print('\nInfelismente o seu pedido de emprestimo foi \033[31mNegado \033[m')
    print(f'* Motivo de emprestimo negado\n>> Valor da parcela\033[31m(R${vParc:.2f})\033[m exede 30% do salario\033[31m(R${vSalario:.2f})\033[m')
    print(f'>> \033[34mFaça uma nova simulaçao alterando a quantidade de parcela para o minimo de\033[31m {qMinAno}\033[34m anos\033[m')
else:
    print(f'Sua solicitação de emprestimo foi \033[32mAprovada\033[m!!')
    print(f'Valor da parcela \033[32mR${vParc:.2f}\033[m')
    print(f'Quantidade de parcelas \033[32m{Qparc} meses\033[m')
