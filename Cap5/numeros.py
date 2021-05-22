def divisores(n):
    #Ejercicio 5.7.7 a)
    acum = 0
    for x in range(1, n): 
        if n % x == 0:
            acum += x
    return acum


def perfectos(): 
    #Ejercicio 5.7.7 b) 
    numero = int(input('Ingrese un nro: '))
    for x in range(1, numero+1): 
        a = divisores(x)
        if x == a: 
            print(x)

perfectos()

def amigos(): 
    #Ejercicio 5.7.7 c)
    numeros= int(input('Ingrese un nro: '))
    for x in range(1,numeros + 1): 
        a = x 
        n1 = divisores(a)
        b = n1
        if b != a:
            n2 = divisores(b)
            if n1 == b and n2 == a:  
                print(a,b, sep=',')

amigos()



    
