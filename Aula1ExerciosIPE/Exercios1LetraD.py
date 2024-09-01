
valor_Em_Real = input('Escreva o valor em Real: ') # input é string, então não é valor numerico ainda!
valor_Em_Real = float(valor_Em_Real)
valor_Da_Taxa_De_Cambio = input('Escreva a taxa de cambio do dola: ')
valor_Da_Taxa_De_Cambio = float(valor_Da_Taxa_De_Cambio)
valor_Final_Converdito = valor_Em_Real / valor_Da_Taxa_De_Cambio
print('')
print(f'Valor covertido é: {valor_Final_Converdito:.2f}')

# Esse algoritmo é bem falido... Não tem lógica de verificação de pontos float ou Caracteres... Entre outra palavras é bem liso :)