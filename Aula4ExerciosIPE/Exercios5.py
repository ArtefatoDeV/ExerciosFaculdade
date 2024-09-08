nome_produto = input('Nome do produto: ')
valor_do_produto = input('Valor do produto: ')
porcetagem_de_desconto = input('Valor do desconto em porcentagem: ')

try:
    valor_do_produto = float(valor_do_produto)
    porcetagem_de_desconto = float(porcetagem_de_desconto)
    print(f'O valor do desconto é: {valor_do_produto * (porcetagem_de_desconto / 100)}') 
    print(f'O valor a pagar é: {valor_do_produto - (valor_do_produto * (porcetagem_de_desconto / 100))}')

except ValueError:
    print('Parece que não é número!')