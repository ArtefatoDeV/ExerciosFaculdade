import math

boas_acoes = input('Quntas boas ações você fez hoje?: ')
print()

try:
    boas_acoes = int(boas_acoes)
except ValueError:
    while boas_acoes.isdigit() == False:
        print('Cara eu desito vc é uma anta kkk. Excreva um número inteiro mas que não seja negativo.')
        boas_acoes = input('Digite novamnete: ')
        try:
            boas_acoes = int(boas_acoes)
            break
        except:
            continue

    boas_acoes = int(boas_acoes) 
    print()

if boas_acoes < 0:
    print(f'Animal digitou negativo né ? Vagabundo... boas AÇÕES NEGATIVAS ? TÁ FAZENDO MALDADE NÉ VADIA.'
         f'\nTem sorte que eu conserto.'
         f'\nVoce quis dizer que {boas_acoes} e positivo né')
    boas_acoes = int('{:.0f}'.format(math.fabs(boas_acoes)))
    print()

if boas_acoes < 5 and boas_acoes > 0:
    print(f'Até que você é uma pessoa boa... ao contrario de mim :)')
    print(f'Números de boas ações: {boas_acoes}\n')
elif boas_acoes == 5:
    print(f'você é uma pessoa carismatica... PAU NO SEU CU, TROXA')
    print(f'Números de boas acoes: {boas_acoes}\n')
else:
    print('TÚ TA ANIMADO EM VAGABUNDO VAI DAR BOGA HOJE NÉ ? GULOSO')
    print(f'Números de boas acoes: {boas_acoes}\n')





        