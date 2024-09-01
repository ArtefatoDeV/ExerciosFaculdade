import math

boas_acoes = input('Quntas boas acoes vc fez hoje?: ')
print()

try:
    boas_acoes = int(boas_acoes)
except:
    while boas_acoes.isdigit() == False:
        print('Cara eu desito vc é anta kkk. Excreva um número inteiro mas que não seja negativo.')
        boas_acoes = input('Digite novamnete: ')

    boas_acoes = int(boas_acoes)
    print()


if boas_acoes < 0:
    print(f'Animal digitou negativo né vagabundo boas ACOES NEGATIVAS ? TA FAZENDO MALDADE NE VADIA\nTem sorte que eu conserto.\nVoce quis dizer que {boas_acoes} e positivo né')
    boas_acoes = int('{:.0f}'.format(math.fabs(boas_acoes)))
    print()


if boas_acoes < 5 and boas_acoes > 0:
    print(f'Ate que vc e pessoa boa a contrario de mim')
    print('Numeros de boas acoes: ')
elif boas_acoes == 5:
    print(f'Vc e pesso carismatica PAU NO SEU CU')
    print('Numeros de boas acoes: ')
else:
    print('TU TA ANIMADO EM VAGABUNDO VAI DAR HOJE KK')
    print(f'Numeros de boas acoes: {boas_acoes} ')





        