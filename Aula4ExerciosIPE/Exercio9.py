nub1 = input(f'Primero número: ')
nub2 = input(f'Primero segundo: ')
nub3 = input(f'Primero terceiro: ')
"""
Lembrando que podemos usar a "funcao max e min"

"""
try:
    nub1 = int(nub1)
    nub2 = int(nub2)
    nub3 = int(nub3)
    
    if nub1 < nub2 and nub1 < nub3:
        print(f'O primeiro numero é menor')
    elif nub2 < nub1 and nub2 < nub3:
        print(f'O segundo é o menor')
    elif nub3 < nub2 and nub3 < nub1:
        print(f'O terceiro numeo é menor')
    else:
        print('empate')

    if nub1 > nub2 and nub1 > nub3:
        print(f'O primeiro numero é maior')
    elif nub2 > nub1 and nub2 > nub3:
        print(f'O segundo é o maior')
    elif nub3 > nub2 and nub3 > nub1:
        print(f'O terceiro numero é maior')
    else:
        print('empate')

except ValueError:
    print('Não é inteiro!')