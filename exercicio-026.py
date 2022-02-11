#Faça um programa que leia uma frase pelo teclado e mostre:quantas vezes aparece a letra 'a',em que posição ela aparece a primeira
# vez,em que posição ela aparece a ultima vez

frase = str(input('Digite uma frese >> ')).strip().lower()
print('Analizando a sua frese ...')
print(f'A letra "a" aparece {frase.count("a")}')
print(f'A letra "a" aparece a primeira vez na posição : {frase.find("a")}')
print(f'A ultima posição que a letra "a" aparece é : {frase.rfind("a")}')