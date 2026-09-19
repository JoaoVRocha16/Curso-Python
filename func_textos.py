# Limpar a tela
from os import system 
system( 'cls')

# Funções para trabalhar com texto
nomecompleto = input('digite seu nome completo: ')

# len = length - conta o número de caracteres
print('- Função para contar caracteres: ', len( nomecompleto))
# upper = transforma o texto em maiúsculo
print('- Função para texto maiuúsculo: ', nomecompleto.upper())
# lower = transforma o texto em minúsculo
print('- função para texto minúsculo', nomecompleto.lower())
# capitalize = trasnforma a primeira letra em maiúsculo
print('- Função para primeiro maiúsculo: ', nomecompleto.capitalize())
# title = trasnforma a primeira letra de cada palavra em maiúsculo
print('- Função para primeira letra de cada palavra maiúcula: ', nomecompleto.title())
# strip = remove os espaços em branco antes e depois do texto 
print('- Função para remover espaços amtes e depois do texto: ', nomecompleto.strip())
espaço = nomecompleto.find(' ')
print('- Primeira letra: ', nomecompleto[0:espaço])

# substituir uma palavra por outra
# novonome = nomecompleto.replace('joao','vitor')
# print(novonome)

print('- Remover espaços vazios: ', nomecompleto.replace(' ',''))
print('- Contar letras sem espaço: ', len(nomecompleto.replace(' ','')))