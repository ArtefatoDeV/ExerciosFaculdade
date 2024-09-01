quitirmaoes = input('Digite quantos irmãoes(números inteiros) são para ver quantos se terá ou não descontos: ')

try:
   quitirmaoes = int(quitirmaoes)
except:
   while quitirmaoes.isdigit() == False:
      print('Você é burro ? Digite um número inteiro... Ou seus filhos é quebrando, caracteres ou negativos ? !!! ')
      quitirmaoes = input('Digite novamente ae boot: ')
      
   quitirmaoes = int(quitirmaoes)

if quitirmaoes > 0 and quitirmaoes < 2:
   print(f'A escola é boa mas, não tera desconto.\nFaz mais couito ae!!')
else:
    print(f'Tera um desconto de 10%\nValeu otário por fazer couito')
