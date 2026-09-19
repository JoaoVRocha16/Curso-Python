from os import system
system('cls')

# calculadora de IMC
# Pede para usuário digitar a altura
altura = input('Digite sua altura em metros: ')
# Substitui vírgula por ponto e converte em decimal
altura = float(altura.replace(',','.'))

# Pede para usuário digitar o peso
# Substitui vírgula por ponto e converte em decimal
peso = input('Digite seu peso em Kg: ')
peso = float(peso.replace(',','.'))

imc = peso / (altura * altura)

# print('seu IMC: {}' . format(imc))
print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso normal')
elif imc < 25:
    print(' Peso normal')
elif imc < 30:
    print('Excesso de peso')
elif imc < 35:
    print('Obesidade classe 1')
elif imc < 40:
    print('Obesidade classe 2')
else:
    print('Obesidade classe 3')
