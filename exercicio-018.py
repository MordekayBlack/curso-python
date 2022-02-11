# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,conseno e tangente desse angulo
import math
grau = int(input('Digite o valor em grau >> '))

#converte em radinus
angulo = math.radians(grau)

# caucula o seno ,conseno e a tangente
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f' O valor digitado foi {grau}\nO valor de seno é {seno:.2f}\nO valor de conseno é {coseno:.2f}\nO valor da tangente é {tangente:.2f} ')