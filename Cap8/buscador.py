def buscar():
    ''' Busca en la lista todos los elementos que coincidan con el pasado por parámetro
    y devuelve la cantidad de coincidencias encontradas''' 
    ld = [1,2,'s',3,'r',3,4,5,1,2,4,'f','s','e',2,2]
    par = 2 
    acum = []
    for x in ld: 
        if x == par: 
            acum.append(x)
    print (len(acum))

buscar() 
def buscare():
    ''' Busca en la lista el primer elemento que  coincide con el pasado por parámetro y devuelve su posición ''' 
    ld = [1,2,'s',3,'r',3,4,5,1,2,4,'f','s','e',2,2]
    par = 2 
    if par in ld: 
        return ld.index(par)

buscare()

def busca():

    ld = [1,2,'s',3,'r',3,4,5,1,2,4,'f','s','e',2,2]
    par = 2 
    for x in ld: 
        if x == par: 
            print(ld.index(x))
            #No hace lo esperado devuelve la posicion del primero

        

busca()