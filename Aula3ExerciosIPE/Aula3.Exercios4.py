print(f'Programa para calcular MEDIA de 4 numeros')
print()


number1 = input('Primeiro número: ')
number2 = input('Segunto número: ')
number3 = input('Segunto número: ')
number4 = input('Segunto número: ')
media = float


try:
    number1= float(number1)
    number2= float(number2)
    number3= float(number3)
    number4= float(number4)
    media = (number1 + number2 + number3 + number4) / 4
    print(f'Olha a media ae: {media:.2f}')
 
except:
    print('Parece que vc digitou string ou seila to com sono para fazer logica')
   
""""
try:
    number1= int(number1)
    number2= int(number2)
    number3= int(number3)
    number4= int(number4)

except:
    while type(number1,str) or type(number2,str) or type(number3,str) or type(number4,str) == True:
        print('Parece que vc digitou algo que não seja INTEIRO DIGITE NOVAMENTE')
        number1 = input('Digite novamente o 1: ')
        number2 = input('Digite novamente o 2: ')
        number3 = input('Digite novamente o 3: ')
        number4 = input('Digite novamente o 4: ')
    
    number1 = int(number1)
    number2 = int(number2)
    number3 = int(number3)
    number4 = int(number4)
    
"""
        
