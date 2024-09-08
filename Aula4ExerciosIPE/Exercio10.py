salario = input('Digite o seu salario: ')
VALORES_ACIMA_DE_1250 = 10
VALORE_IGUAS_OU_ABAIXO_DE1250 = 15
teste = None

try:
    salario = float(salario)
    if salario > 1250:
        print(f'Aumento é: {salario + (salario * (VALORES_ACIMA_DE_1250 / 100))}')
        print(teste)
    else:
        print(f'Aumento é: {salario + (salario * VALORE_IGUAS_OU_ABAIXO_DE1250 / 100)}')
        teste = True
        print(teste)
except ValueError:
    print('Não é numero!')