from os import system
system('cls')

# Inicia a contagem do 'multiplicando'
for i in range(1,11):
# Limpa a variavel 'linha'
    linha = ''
    for ii in range(1,11):
        # Vai armazenando toda a tabuada
        linha += f'{i*ii: >4} ' # >4 = Totaliza 04 caracteres, completando com espaço vazio
        # Mostra os resultados da tabuada do 'multiplicando'
    print(linha) 