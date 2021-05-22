def diccionariocontador(): 
    cadena = ("que lindo día que hace hoy ").split()
    a = 0
    diccionario = {}

    for x in cadena:  
        if x not in diccionario:
            diccionario[x] = a +1
        else: 
            l = diccionario.pop(x)
            diccionario[x] = l +1

    
    print(diccionario)

diccionariocontador()
#cuenta las apariciones pero las que se repiten devuelve en la posicion de la última 
def diccionariocontadorl(): 
    cad = ("que lindo día que hace hoy ")
    diccionario = {}

    for x in cad:  
        if x not in diccionario:
            diccionario[x] = 1
        else: 
            l = diccionario.pop(x)
            diccionario[x] = l +1

    
    print(diccionario)

diccionariocontadorl()

def dados():
    import random
    dado = (1,2,3,4,5,6)
    iteracion = int(input('Nro de iteraciones: '))
    diccio = {}
    for x in range (iteracion):  
        resultado = random.choice(dado) + random.choice(dado)
        if resultado not in diccio:
            diccio[resultado] = 1 
        else: 
            l = diccio.pop(resultado)
            diccio[resultado] = l + 1
    print(diccio)

dados()


