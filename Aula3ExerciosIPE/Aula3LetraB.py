quantidade_de_alunos = input('Qual é quantidade de alunos ?: ')

try:
    quantidade_de_alunos = int(quantidade_de_alunos)
except:
    while quantidade_de_alunos.isdigit() == False:
        print('Novamente boot dms... Colocar INT PELA AMOR DE GOD USER')
        quantidade_de_alunos = input('Digite novamente em inteiro: ')
    
    quantidade_de_alunos = int(quantidade_de_alunos)

if quantidade_de_alunos > 30 and quantidade_de_alunos > 0:
    print('Parabens Voces ganharão uma viaje de bosta para "CANCUN"')
elif quantidade_de_alunos == 30:
    print('Os troxas ganharam passem para "Fortaleza"')
elif quantidade_de_alunos < 30 and quantidade_de_alunos > 0 :
    print('Os bot ganharao para "Caldas novas"')
else:
    print('POR VCS SÃO "ARTHUR" ??? POR COLOCAREM NEGATIVOS VAO GANHAM PASSAGEM PARA PUTA Q PARIU####')