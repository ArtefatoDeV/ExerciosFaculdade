nome = 'Isaque Fernandes'
peso = 58

print(hex(id(nome))) # Id = indentificador.. Significa o endereço da memoria.
print(hex(id(peso))) # hex é "função" que, calcular o endereço de memoria em hexadencimal.
print(bin(id(nome))) # Em binario
print(oct(id(nome))) # Em oct
print(id(nome)) # Sem ser hex... é tudo int então é de boa fazer a conta.
print()
print(type(nome)) # type verifica tipo imutavel da variavel.
print(type(peso)) # type verifica tipo imutavel da variavel.
print()

print('Soma:','\n',12, sep='')