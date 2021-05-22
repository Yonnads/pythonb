#Ejercicio 6.8.2
def sepa():
    cadena = input('Ingrese una palabra: ')
    separador = input('Ingrese el separador: ')
    acumulado = ''
    for x in cadena:
        
        a = x + separador
        acumulado += a

    print (acumulado)

sepa()

def espa():
    cad = input('Ingrese una frase: ')
    separ = input('Ingrese el separador: ')
    cadenanueva = ''
    for x in cad:
        if x == ' ':
            cadenanueva += separ
        else: 
            cadenanueva += x

    print (cadenanueva)

espa()

def xxx():
    caden = input('Ingrese el texto: ')
    reemplace = 'X'
    cadenanueva = ''
    numeros = '1234567890'
    for x in caden:
        if x in numeros:
            cadenanueva += reemplace
        else: 
            cadenanueva += x

    print (cadenanueva)

xxx()

def cadenum():
    cades = input('Ingrese los dígitos: ')
    for x in cades[0::3]:
        print (cades)
#Esta función no realiza lo solicitado
cadenum()



    
