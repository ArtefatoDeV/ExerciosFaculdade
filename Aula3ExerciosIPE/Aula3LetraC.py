DESCONTO_DE__PORCENTO1 = 10
DESCONTO_DE__PORCENTO2 = 7
DESCONTO_DE__PORCENTO3 = 4 
VALOR_ABSOLUTO_100 = 100

print('Digite o valor da compra:')
valor_compra = input('Valor: ')

try:
    valor_compra = float(valor_compra)
    if valor_compra > 150.00:
        print(f'O novo valor com o deconto de {DESCONTO_DE__PORCENTO1}% é: {valor_compra - ((DESCONTO_DE__PORCENTO1 / VALOR_ABSOLUTO_100) * valor_compra)}')
    elif valor_compra == 150.00:
        print(f'O novo valor com o deconto de {DESCONTO_DE__PORCENTO2}% é: {valor_compra - ((DESCONTO_DE__PORCENTO2 / VALOR_ABSOLUTO_100) * valor_compra)}')
    elif valor_compra < 150.00 and valor_compra > 0:
        print(f'O novo valor com o desconto de {DESCONTO_DE__PORCENTO3}% é: {valor_compra - ((DESCONTO_DE__PORCENTO3 / VALOR_ABSOLUTO_100) * valor_compra)}')
    else:
        print(f'Voce digitou um número negativo ou 0')
except:
    print('Voçe é boot não digitou caractere ou nada !!!!')
     
    
    
    