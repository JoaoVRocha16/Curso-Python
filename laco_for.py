from os import system
import time
system('cls')

numero = int(input('Informe um número maior que 0:'))

if numero <= 0:
    print('Número inválido!')
else:
    # Iniciando laço for
    for i in range(numero):
        print(f'Valor da variável i: {i}')
        time.sleep(1)
