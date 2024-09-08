km_dias = input(f'Digite os km percoridos: ')
dias_rodados = input(f'Digite os dias alugados: ')

try:
    km_dias = int(km_dias)
    dias_rodados = int(dias_rodados)
    print(f'Valor a pagar pelos km rodados pelos dias alugados: {km_dias * 0.15}')
    print(f'O Valor a pagar pelos dias rodados é {dias_rodados * 60}')
except ValueError:
    print('Parece que não é número!')