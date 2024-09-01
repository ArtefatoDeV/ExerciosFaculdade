VERIFICACAO_PONTOS = 5
pontos_digitados = 0

pontos_digitados = input(('Vamos calcular os seu pontos. É diate vamos te falar...: '))

try:
    pontos_digitados = int(pontos_digitados)
except:
    while pontos_digitados.isdigit() == False:
        print('Bot novamente pois não digitou um numero inteiro ou negativos!')
        pontos_digitados = input('Digite novamente meu amigo: ')
    
    pontos_digitados = int(pontos_digitados)
    print()

if pontos_digitados < VERIFICACAO_PONTOS and pontos_digitados >= 0:
    print('Apesar de ser um otario na rua pela lei vc ("E BOM CONDUTOR")')
elif pontos_digitados == VERIFICACAO_PONTOS:
    print('Apesar de ser um bom condutor tome cuidado!')
elif pontos_digitados > VERIFICACAO_PONTOS:
    print('Voce não é legal... vai SE FUDER... E TOME MULTA')
else:
    print('Digitou numero negativo de DESGRACADO')
