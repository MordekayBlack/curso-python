#Desenvolva um programa que pergunte a distancia de uma viagem em km,caucule o preço da passagem cobrando R$0,50 centavos por viagem ate 200km,
  #  e R$0,45 para viagem acima de 200km

dist = int(input('Qual é a distancia/Km da viagem? >> '))

if dist < 200:
    valor = float(dist * 0.50)
    print(f'A distancia/km de sua viagem é de {dist}km.\nSerá cobrado o valor de R$0,50 por km.\nO valor total da viagem será de R${valor}')
else:
    valor = float(dist * 0.45)
    print(f'A distancia/km de sua viagem é de {dist}km.\nSerá cobrado o valor de R$0,45 por km.\nO valor total da viagem será de R${valor:.2f}')