velocidade_km = input('A velocidade que estava SEM MENTIR É: ')
VELOCIDADE_MAX = 80
try:
    velocidade_km = int(velocidade_km)
    if velocidade_km > VELOCIDADE_MAX:
        print(f'Multa a pagar pelo velocidade ultrapassada é {(velocidade_km - VELOCIDADE_MAX) * 5}')
        print(f'Velocidade que estava {velocidade_km}')
    else:
        print(f'Tava no permetido {velocidade_km}km')
except ValueError:
    print(f'Não e inteiro')