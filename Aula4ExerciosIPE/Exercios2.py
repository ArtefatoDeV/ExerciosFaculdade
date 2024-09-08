metros = input('Digite um valor em metros para converter para melimetros: ')

try:
    metros = float(metros)
    print(f'O valor em metros convertido a melimetros é: {metros * 1000:.0f} milimetros') #Para tranforma metro em melimetro faz metros * 1000
except ValueError:
    print('Não digitou numeros')
    