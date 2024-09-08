km_rodados = input('Quantos km vc vai andar: ')
VALORES_COST_ACIMA_DE_200KM = 0.45
VALORES_COST_ABXIO_OU_IGUAL_DE_200KM = 0.50
texte = None
try:
    km_rodados = int(km_rodados)
    if km_rodados > 200:
        print(f'O valor a ser pago pelos km:{km_rodados} é: {km_rodados * VALORES_COST_ACIMA_DE_200KM}')
        print(texte)
    else:
        print(f'O valor a ser pado pelos km:{km_rodados} é : {km_rodados * VALORES_COST_ABXIO_OU_IGUAL_DE_200KM}')
        texte = True
        print(texte)
except ValueError:
    print('Parece que não é inteiro')
