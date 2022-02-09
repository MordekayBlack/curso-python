#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informaçoes possiveis sobre ele

v = input('Digite algo : ')

print(f'\nO tipo primitivo do valor digitado é {type(v)}')
print(f'O valor digitado é um numero {v.isnumeric()}')
print(f'O valor digitado é alpha numerioo {v.isalnum()}')
print(f'O valor digitado esta em munusculo  {v.islower()}')
print(f'O valor digitado esta em maiuculo {v.isupper()}')