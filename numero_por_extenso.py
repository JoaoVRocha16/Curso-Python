from os import system
system('cls')

numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

numero = int(input('Digite um número entre 0 e 99: '))

if numero>= 0 and numero <= 99:
    if numero < 10:
        print(f'Número por extenso: {numeros[numero]}')
    elif numero < 20:
        print(f'Número por extenso: {dez[numero-10]}')
    else:
        unidade = numero % 10
        dezena = numero // 10
        if unidade == 0:
            print(f'Número por extenso: {dezenas[dezena-2]}')
        else:
            print(f'Número por extenso: {dezenas[dezena-2]} e {numeros[unidade]}')

else:
    print('Número inválido!')