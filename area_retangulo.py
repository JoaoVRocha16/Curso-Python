# Calcula a área de um retangulo
# float = ponto flutuante, ou seja, aceita casas decimais
# Utilizar . como ,
base = input('Informe a base do retangulo: ')
altura = input(' Informe a altura do retangulo: ')

print('Base é numerico? ', base.isnumeric())
print('Altura á numerico? ', altura.isnumeric())


area = float(base) * float(altura)

# print('base: {}, Altura: {}, Area: {}' . format(base,altura,area))
print('A área do retangulo é de: ', area)