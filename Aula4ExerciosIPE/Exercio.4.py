salario = input('Salario atua: ')
porcentagem = input('Porcentagem: ')

try:
    salario = float(salario)
    porcentagem = float(porcentagem)

    print(f'Novo aumneto: {(salario * (porcentagem / 100)):.2f}')
    print(f'Novo salario: {salario + (salario * (porcentagem /100)):.2f}')

except ValueError:
    print('Digite um numero kk')