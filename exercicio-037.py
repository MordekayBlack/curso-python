#   Escreva um programa que leia um numero inteiro qualquer,e peça para o usuario escolher qual a base de conversao,
#    1:binario , 2:octal , 3:hexadecimal
conv = ' '
print(f'{" Menu ":=^30}')
print('''1: Converter em Binário 
2: Converter em Octal  
3: Converter em Hexadecimal ''')

opcao = int(input('Qual operação deseja realizar?  >> '))
nConv = 0
if opcao == 1 or opcao == 2 or opcao == 3:

    n = int(input('Digite o valor que deseja converter >> '))
    if opcao == 1 :
        nConv = format(n,"b")
        conv = 'Binario'
    elif opcao == 2:
        nConv = format(n,"o")
        conv = 'Octal'
    elif opcao == 3:
        nConv = format(n,"x")
        conv = 'Hexadecimal'
    print(f'O valor \033[32m{n}\033[m convertido em \033[32m{conv }\033[m =\033[32m {nConv} ')
else:
    print('Opção inválida.Tente novamente.')
