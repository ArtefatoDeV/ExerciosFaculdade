"""
print("Arredondamento para cima:", math.ceil(2.5)) # Arredonda para cima: 3
print("Arredondamento para baixo: ", math.floor(2.5)) # Arredonda p/ baixo: 2 
print("Valor absoluto: ", math.fabs(-2.5)) # Valor absoluto: 2.5 
print("Fatorial: ", math.factorial(4)) # Fatorial: 24 
print("Maior divisor comum: ", math.gcd(4, 6)) # Maior divisor comum: 2 
print("Raiz quadrada: ", math.sqrt(64)) # Raiz quadrada: 8.0 
print("Logaritmo: ", math.log(10, 5)) # Logaritmo: 1.4306765580733933 
print("Seno: ", math.sin(30)) # Seno: -0.9880316240928618 
print("Coseno: ", math.cos(30)) # Coseno: 0.15425144988758405 
print("Tangente: ", math.tan(30)) # Tangente: -6.405331196646276 
print("Seno em graus: ", math.sin(math.radians(30))) #Seno em graus: 0.49999999999999994 
print("Coseno em graus: ", math.cos(math.radians(30))) #Coseno em graus: 0.8660254037844387 
print("Tangente em graus: ", math.tan(math.radians(30))) # Tangente em graus: 0.5773502691896257 

print("PI: ", math.pi) # PI: 3.141592653589793

"""
import math

ANGULO_DE_45 = 45  #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...
ANGULO_DE_60 = 60  #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...
ANGULO_DE_90 = 90  #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...
ANGULO_DE_180 = 180 #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...
ANGULO_DE_270 = 270 #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...
ANGULO_DE_360 = 360 #Estou usando uma CONSTANTE para fixar na cabeça.. No python não uma DECLARAÇÃO DE CONSTANTE  mas, a comunidade colocou que toda VARIAVEL MAIÚSCULA é uma constante...

print(f'Vamos calcular o seno, cosseno, e tagente do angulo {ANGULO_DE_45}.')
print()
print(f'Calculando em o seno de {ANGULO_DE_45} = {math.sin(ANGULO_DE_45)}')
print(f'Calculando o cosseno de {ANGULO_DE_45} = {math.cos(ANGULO_DE_45)}')
print(f'Calculando o tagente de {ANGULO_DE_45} = {math.tan(ANGULO_DE_45)}')
print()
print(f'Calculando o radiano de {ANGULO_DE_45} = {(math.radians(ANGULO_DE_45))}')
print()
print(f'Calculando o SENO em graus do {ANGULO_DE_45} = {math.sin(math.radians(ANGULO_DE_45))}')
print(f'Calculando o COSSENO em graus {ANGULO_DE_45} = {math.cos(math.radians(ANGULO_DE_45))}')
print(f'Calculando o tagente em graus {ANGULO_DE_45} = {math.tan(math.radians(ANGULO_DE_45))}')
print('\n')
print(f'Vamos calcular o seno, cosseno e tagente do angulo {ANGULO_DE_60}.')
print()
print(f'Vamos calcular o seno de {ANGULO_DE_60} = {math.sin(ANGULO_DE_60)}')
print(f'Vamos calcular o cosseno de {ANGULO_DE_60} = {math.cos(ANGULO_DE_60)}')
print(f'Vamos calcular o tagenet do {ANGULO_DE_60} = {math.tan(ANGULO_DE_60)}')
print(f'Vamos calcular em radianos do {ANGULO_DE_60} = {math.radians(ANGULO_DE_60)}')
print(f'Vamos calcular o SENO EM GRAUS de {ANGULO_DE_60} = {math.sin(math.radians(ANGULO_DE_60))}')   # Para calcular em GRAUS seja sin, cos ou tan... Deve primeiro par pelo RADIANS 
print(f'Vamos calcular o COSSENO EM GRAUS de {ANGULO_DE_60} = {math.cos(math.radians(ANGULO_DE_60))}') # Para calcular em GRAUS seja sin, cos ou tan... Deve primeiro par pelo RADIANS 
print(f'Vamos calcular o TAGENTE EM GRAUS de {ANGULO_DE_60} = {math.tan(math.radians(ANGULO_DE_60))}') # Para calcular em GRAUS seja sin, cos ou tan... Deve primeiro par pelo RADIANS 
print('\n')
print(f'Vamos calcular o angulo de {ANGULO_DE_90} pata Seno , cosseno e tagente')
print()
print(f'Vamos calcular o seno do {ANGULO_DE_90} = {math.sin(ANGULO_DE_90)}')
print(f'Vamos calcular o cosseno do {ANGULO_DE_90} = {math.cos(ANGULO_DE_90)}')
print(f'Vamos calcular o tangente do {ANGULO_DE_90} = {math.tan(ANGULO_DE_90)}')
print()
print(f'Vamos calcular o radino do {ANGULO_DE_90} = {math.radians(ANGULO_DE_90)}')
print('Vamos calcular o o SENO, COSSENO E TAGENTE EM GRAUS')
print()
print(f'Vamo calcular o SENO EM GRAUS do {ANGULO_DE_90} = {math.sin(math.radians(ANGULO_DE_90))}')
print(f'Vamos calcular o COSSENO EM GRAUS do {ANGULO_DE_90} = {math.cos(math.radians(ANGULO_DE_90))}')
print(f'Vamos calcular o TAGENTE EM GRAUS do {ANGULO_DE_90} = {math.tan(math.radians(ANGULO_DE_90))}')


#Vamo ter que relembrar o passado da matematica kkk
#Porque fiquei jogando truco kkkk

