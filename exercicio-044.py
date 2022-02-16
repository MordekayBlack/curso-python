'''    Elabore um programa que calcule um valor a ser pago por um produto considerando seu preço normal e condição de pagamento:
    A vista dinheiro/check 10% de desconto
    A vista no cartao debito 5% de desconto
    Até 2x no cartao credito preço normal
    3x no cartao creditp 20% de juros
'''

preco = float(input('Digite o valor do produto >>R$ '))

print(f'{" Formas de Pagamento ":=^50}')
print(''' 1: A Vista Dinheiro / Cheque 10% desconto
 2: A Vista Carão Débito 5% desconto
 3: Até 2x no cartao credito preço normal
 4: 3x no cartao credito' 20% juros''')
print(f'{"=" * 50}')
opcao = int(input('Qual a forma de pagamento desejada? '))

print(f'{"=" * 50}')

if opcao == 1:
    print(f'Preço normal do produto R$ {preco:.2f}')
    print(f'Desconto de R${ preco * 10 / 100:.2f} ')
    print(f'Preço final do produto R${preco - (preco * 10 / 100):.2f}')
elif opcao == 2:
    print(f'Preço normal do produto R$ {preco:.2f}')
    print(f'Desconto de R${ preco * 5 / 100:.2f} ')
    print(f'Preço final do produto R${preco - (preco * 5 / 100):.2f}')

elif opcao == 3:
    print(f'Preço normal do produto R$ {preco:.2f}')
    print(f'2X de R${preco / 2:.2f}')
elif opcao == 4:
    print(f'Preço normal do produto R$ {preco:.2f}')
    print(f'Total de juros R${ preco * 20 / 100:.2f} ')
    print(f'Preço final do produto R${preco + (preco * 20 / 100):.2f}')

print(f'\n{" Obrigado Pela Preferência!! ":=^50}')
