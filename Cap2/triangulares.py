def triangulares(): 
    #Ejercicio 2.6.8
    ''' el programa le pide al usuario un nro n, e imprime los primeros nros triangulares
    junto con su indice'''
    a = int(input('Ingrese un nro entero: '))
    acumulado = 0 
    for x in range(1, a+1): 
        acumulado += x

        print (x,acumulado, sep='-')

triangulares()

def triangulos(): 
    numero = (input('ingrese un nro entero: '))
    a = int(numero)
    

    for n in range(1, a +1):
        a = int(((n +1) * n) / 2)
        
        print(n,a, sep='-')

triangulos()
