temperatura_c = input('Digite uma temperatura em [Cº]: ')

try:
    temperatura_c = float(temperatura_c)
    print(f'Valor em [Cº] para [Fº] é: {(9 * temperatura_c / 5) + 32}')
except ValueError:
    print(f'Parece que não e é numero')