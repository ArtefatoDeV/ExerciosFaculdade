nome = 'Isaque fernandes'

nova_string = ''
cont = 0
print(len(nome))

while cont <= len(nome) - 1 :
    nova_string += '*' + nome[cont]
    cont += 1 

print('\n' * 10 )
print(nova_string ,' ', end='$')