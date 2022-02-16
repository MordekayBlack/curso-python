#    Faça um programa que calcule a soma de todos os numeros ipares,e que são multiplos de 3 ,que se encontram no intervalo
  #  de 0 a 500

for c in range(1,500,2):
    if c % 3 == 0:
        print(c, end=' -> ')