numero1 = 0
numero2 = 0
ope = ''

while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    print()


    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except ValueError:
        print('Ops parece que vc não digitou um número!')
        print()
        continue

    operacoes_validadas = '+-/*'
   
    ope = input('Digite umas da operaçãoes validas [+] [-] [*] [/]:')

    if ope not in operacoes_validadas:
        print('Não é uma operação valida! Ou é mais que uma opção!')
        print()
        continue

    if ope == '+':
        print(f'Os números somado é: {numero1 + numero2}')
    elif ope == '-':
        print(f'Os números subtraidos é: {numero1 - numero2}')
    elif ope == '/':
        print(f'Os número divididos é {numero1 / numero2}')
    elif ope == '*':
        print(f'Os números multiplicados é {numero1 * numero2}')
    else:
        print('Nunca é para chegar aqui ')
        continue

   