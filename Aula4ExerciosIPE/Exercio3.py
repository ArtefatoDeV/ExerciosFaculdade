dias = input(f'Digite alguma contidade de dias: ')
horas = input(f'Digite alguma contidade de horas: ')
minutos = input('Digite alguma contidade de segundos: ')

try:
    dias = int(dias)
    horas = int(horas)
    minutos = int(minutos)
    
    print(f'Toda a carga horaria em segundos {dias} em horas {dias * 24} , {horas} em minutos {horas * 60}'
          f'{minutos} em segunto')
    print(f'Todo o tempo em segundos = {(60 * (60 * (dias * 24))) + (60 * (horas * 60)) + (minutos * 60)}')
except ValueError:
    print('Não é numero!')

