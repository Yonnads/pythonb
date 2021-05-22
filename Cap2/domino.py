def fichas(): 
    #Ejercicio2.6.10
    for x in range(7):
        for n in range(x,7 ): 
            print(x,n)

fichas()

def domino():
    #Ejercicio 2.6.11
    n = int(input('nro: '))
    for x in range(n+1): 
        for l in range(x,n+1): 
            print(x,l)

domino()