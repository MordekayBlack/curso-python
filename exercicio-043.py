'''    Desenvolva um programa que leia o peso e a altura de uma pessoa,calcule seu imc e mostre o resultado de acordo com a tabela abaixo:
    Abaixo de 18.5 abaixo do peso
    Entre 18.5 e 25 peso ideal
    Entre 25 e 30 sobrepeso
    Entre 30 e 40 obsidade
    acima de 40 obsidade morbida'''

nome = str(input('Digite seu nome >> ')).strip().title()
peso = float(input('Digite seu peso >> '))
altura = float(input('Digite sua altura >>')) / 100


#IMC = Peso ÷ (Altura × Altura)

imc = peso / (altura * altura)

if imc  < 18.5:
    print(f'Fique atento Sr(a) {nome} ,você esta abaixo do peso ideal, o cauculo do seu IMC foi {imc:.2f}')
elif imc >= 18.5 and imc <= 25:
    print(f'Parabens!! Sr(a) {nome} ,você esta com peso ideal, o cauculo do seu IMC foi {imc:.2f}')
elif imc > 25 and imc <= 30:
    print(f'Não se preocupe mas fique atento Sr(a) {nome} ,você esta com sobrepeso, o cauculo do seu IMC foi {imc:.2f}')
elif imc > 30 and imc <= 40:
    print(f'Precisa se cuidar e se exercitar Sr(a) {nome} ,você esta obsidade, o cauculo do seu IMC foi {imc:.2f}')
else:
    print(f'Procure uma orientação medica urgente Sr(a) {nome} ,você esta com obsidade morbida, o cauculo do seu IMC foi {imc:.2f}')