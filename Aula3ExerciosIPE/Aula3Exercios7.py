print('Vamos verificar os seus dados')
nome = input('Digite seu nome: ')
Endereco = input('Excreva seu endereco: ')
Numero_da_residencia = input('Escreva o número da sua casa EM INTEIRO: ')

try:
    Numero_da_residencia = int(Numero_da_residencia)
except:
    while Numero_da_residencia.isdigit() == False:
        print('Cara vai se FUDER kkk burro dems')
        Numero_da_residencia = input('Digite novamente: ')
        print()
    Numero_da_residencia = int(Numero_da_residencia)

if Numero_da_residencia < 65 and Numero_da_residencia > 0:
    print(f'Seu nome é {nome}')
    print(f'Seu endereço é {Endereco}')
    print('você pagará o IPTU deste ano parcelado em 3 vezes ')
elif Numero_da_residencia == 65:
    print(f'Seu nome é {nome}')
    print(f'Seu endereço é {Endereco}')
    print('você pagará o IPTU em duas parcelas')
elif Numero_da_residencia > 65:
    print(f'Seu nome é {nome}')
    print(f'Seu endereço é {Endereco}')
    print('você pagará o IPTU à vista')
else:
    print('Nem vou vou fazer a logica do negativo vai se FUDER boot')
