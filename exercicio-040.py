'''    Crie um programa que leia duas notas e calcule a media,mostrando uma mensagem final de acordo com a media obtida:
    Media abaixo de 5.0 reprovado
    Media entre 5.0 e 6.9 recuperação
    media acima de 7.0 aprovado'''

nome = input('Digite o nome do aluno >> ').strip().title()
n1 = float(input('Digite a primeira nota >> '))
n2 = float(input('Digite a segunda nota >> '))
n3 = float(input('Digite a terceira nota >> '))
n4 = float(input('Digite a quarta nota >> '))

media = (n1 + n2 + n3 + n4) / 4
if media <= 5.0:
    print(f'Ops!Infilezmente, o aluno {nome} foi \033[31mREPROVADO\033[m.')
    print(f'A media obtida entre a 4 notas foi de \033[31m{media}')
elif media > 5.0 and media < 6.9:
    print(f'Ops!Infilezmente, o aluno {nome} foi \033[33mRECUPERAÇÃO\033[m.')
    print(f'A media obtida entre a 4 notas foi de \033[33m{media}')

else:
    print(f'Parabens! O aluno {nome} foi \033[32mAPROVADO\033[m.')
    print(f'A media obtida entre a 4 notas foi de \033[32m{media}')