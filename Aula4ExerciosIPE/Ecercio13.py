import math

TAXA_RESIDE_MAXIMA  = 0.40
LIMIT_RESIDE_MAXIMA = 500
TAXA_RESIDE_ACIMA_MAXIMA = 0.65

TAXA_COMER_MAXIMA = 0.55
LIMIT_COMER_MAXIMA = 1000
TAXA_COMER_ACIMA_MAXIMA = 0.60

TAXA_INDRUS_MAXIMA = 0.55
LIMIT_INDRUS_MAXIMA = 5000
TAXA_INDRS_ACIMA_MAXIMA = 0.60

consumo_kWh = 0
opecao = ''

while True:
    
    opecao_validades = 'cri'
    opecao = input('Digite alguma das opções [R] para residencial [C] para comercial [I] para indrus: ').lower()
    print()

    if opecao not in opecao_validades:
         print('Digite uma opção valida!')
         print()
         continue

    consumo_kWh = input('Por favor digite seu consumo de [KWH]: ')
    print()
    
    try:
        consumo_kWh = int(consumo_kWh)
        if consumo_kWh < 0:
            i = 0
            confime = 's'
            print(f'Ops parece que você digitou um número negativo!\n'
                 f'Temos noção que pode acontecer MAS como acontecu "UM ERRO" gostarimo de avisas...\n'
                 f'Pode ficar traquilo que vamos arrumalo!\n'
                 f'MAS gostarimos de saber se você esta ciente.\n'
                 f'Digite [S] para continuar ou [N] para reiniciar!')
            print()
            for i in range(0,3):
                   confime = input('Digite para confimar [S] para sim-confirmo [N] para não-confirmo!').lower()
                   if confime == 's':
                        print('Ok, iremos arrumar o erro!')
                        print()
                        consumo_kWh = int('{:.0f}'.format(math.fabs(consumo_kWh)))
                        break
                   elif confime == 'n':
                        print('Ok vamos renicias')
                        continue
                   elif i == 2:
                        print(f'Caraba parece que ainda não entendeu mas fique traquilo o programa reniciara com 3 tentativas com erro!')
                        print(f'Agora você está com {i + 1} erros!')
                        print()
                
                   if i == 2:
                       print()
                       print(f'Reniciamos para você o programa DE NADA!')
                       print()
                       continue
    except ValueError:
        print(f'Por favor!\n'
             f'Digite o valor em número que não contenha CARACTERES!')
        print()
        continue

    if opecao == 'c' and consumo_kWh <= LIMIT_COMER_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_COMER_MAXIMA)}')
         print()

    elif opecao == 'c' and consumo_kWh > LIMIT_COMER_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_COMER_ACIMA_MAXIMA)}')
         print()

    elif opecao == 'i' and consumo_kWh <= LIMIT_INDRUS_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_INDRUS_MAXIMA)}')
         print()

    elif opecao == 'i' and consumo_kWh > LIMIT_INDRUS_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_INDRS_ACIMA_MAXIMA)}')
         print()

    elif opecao == 'r' and consumo_kWh <= LIMIT_RESIDE_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_RESIDE_MAXIMA)}')
         print()

    elif opecao == 'r' and consumo_kWh > LIMIT_RESIDE_MAXIMA:
         print(f'O valor a ser pago é: {consumo_kWh + (consumo_kWh * TAXA_RESIDE_ACIMA_MAXIMA)}')
         print()
    

    

    