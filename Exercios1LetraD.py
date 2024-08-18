#Bom como Fernando não completou a questão eu vou completar pro mim mesmo.

valor_Em_Real = input('Escreva o valor em Real: ')      # input é string então não valor numerio ainda
valor_Em_Real = float(valor_Em_Real)
valor_Da_Taxa_De_Cambio = input('Escreva a taxa de cambio do dola: ')
valor_Da_Taxa_De_Cambio = float(valor_Da_Taxa_De_Cambio)
valor_Final_Converdito = valor_Em_Real / valor_Da_Taxa_De_Cambio
print('')
print(f'Valor covertido é: {valor_Final_Converdito:.2f}')

# Esse algoritimo é bem falido... Não tem lógica de verificação de pontos ou seja liso :)