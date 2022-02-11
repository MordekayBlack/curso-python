# Façã um progrema que leia o cumprimento do cateto oposto e do cateto adjacente de um triagulo,caucule e mostre
#     o cumprimento da hipotenuza
from math import hypot
cO = float(input('Digite o valor do cateto oposto >> '))
cA = float(input('Digite o valor do cateto adjacente >> '))

result = hypot(cO,cA)
print(f'O valor da hipotenuza é {result:.2f}')