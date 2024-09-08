num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f'Soma de dos numeros: {num1 + num2}')
except ValueError:
    print('Animal digitou caracter')
