""""
dados = [] 
crifr = []
dadoscrif = [None] * 10

dados.append(1)
dados.append(2)
dados.append(3)
dados.append(4)
dados.append(5)
dados.append(6)
dados.append(7)
dados.append(8)
dados.append(9)
dados.append(10)

crifr.append('!')
crifr.append('@')
crifr.append('#')
crifr.append('$')
crifr.append('%')
crifr.append('&')


print()
print(dados)
print()

troca = dados[0]

for i in range(len(dados)):
    if len(dados) - 1 != 0:
        dados[i] = len(dados) - i  
    else:
        dados[len(dados)] = troca

print(dados)

"""
""""
lista1 = [55,23,34] #Declaração de lista.
copia = lista1 #Uma lista(Que é um tipo de 'variavel' Pode ser inseriada em uma variavel)
print(lista1)
print(copia)
print()
lista1.append(15) # O comando append(valor) vai inserio o 'valor' no proximo indeci =
print(len(lista1)) # Me volta tanto em lógica ou no print quantidade 'indici na lista  OBS ELE VAI COMEÇAR DO 1'
print(min(lista1)) # Retorna o menor valor da lista 'int' POR ENQUANTO.
print(max(lista1)) # Retorna o maior valor da lista 'int' POR ENQUANTO.
print(sum(lista1)) # Retorna a SOMA de todos os elementos da lista.
print()

lista2 = [2,3,4,5]

print(f'Lista 2 = {lista2}')
lista3 = [4,3,5,4]
print(f'Lista 3 = {lista3}')
lista2.extend(lista3) # A funcao extend(valor) vai adicionar em lista outra lista deois da lista 1; LEMBRANDO QUE NÃO E SO LISTA QUE PODE SER JUNTADA PODE SER QUALQUE COISA
print(f'Lista 2 com adição da lista 3 = {lista2}')
print()

lista4 = ['Unip','Ciências da computação'] # Nesse exeplo acho que foi para dizer que STRING e INT pode ser juntadas
lista5 = [2024,2025]
lista4.extend(lista5)
print(lista4)
print()

lista6 = ['nome', 'senha', 1,2,3,4]
lista6.extend('Senha nova') # nesse caso cada LETRA VAI SER INTERPRETADO COMO INDICE... Então não vai ser uma string junta.
print(lista6)
print()
print('Para colocar em "STRING JUNTA", VC deve colocar um COCHETE lista6.extend(["Senha nova"])')
lista6.extend(['Senha nova'])
print(lista6)
print()

lista7 = [1,2,3,4,5]
lista7.insert(1,'Bancon') # O insert NÃO VAI 'MATAR' o que estar no indice que vc selecionar ele so vai encaixar.
print(lista7)
print(len(lista7)) # verificaçao do tamanho da lista.
print()

"""
""""
lista8 = ['java','C#','PHP','Python','NET']
lista8.insert(0, 'C++') #Lembra que o insert não mata o que estiver na string
print(lista8[2])
print()

lista9 = ['java','python','c#','PHP'] # PRIMERA INSTACIA
lista9.pop(0) # O pop vai servir para eliminar pelo indice e NÃO PELO QUE ESTA ARMAZENADO NA POCIÇAO.
print(lista9)
print()

lista10 = ['java','python','c#','PHP','python']
print(lista10)
lista10.remove('python') # O remove vai remover NÃO PELO INDICE MAIS PELO QUE ESTA ARMAZENADO NO INCI DA ""DA ESQUERDA PARA DIREITA É SO UMA VEZ"" 
print(lista10)
print()

lista11 = ['java','python','c#','PHP','python']
lista11.sort() # A funçao sort faz, lista ficar na ordem cresente.
print(lista11)
print()

lista11.reverse()
print(lista11) # Faz a lista ficar a contraria OBS: ordem reversa da lista, NÃO É ORDENAÇÃO DECRESCENTEm.
print()

print('Para fins dadicos para fazer uma lista DECREZENTE VC PODE CHAMAR  FUNÇÃO sort() e depois aplicar a função reverse()')
lista12 = [2,11,3,7,9]
print()
lista12.sort()
print(lista12)
lista12.reverse()
print(lista12)
print()

lista13 = ['java','python','c#','PHP','python']
print(lista13.count('python')) # A função count('Valor') serve para verificar quantos dados IGUAS TEM EM UMA LISTA COUNT COUNT.
# print(' * 2)

"""

lista_funcoes = []
print('Digite todas a funcoes que vc apredeu nessa slind:')

final = 'n'
cont = 0
while final != 's':
    final = input('Qual função: ')
    lista_funcoes.insert(cont,final)
    final = input('Vai finalizar ?: ')
    cont += 1

print(lista_funcoes)