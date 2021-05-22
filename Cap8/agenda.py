def agenda_simplificada():
    '''La función recibe una cadena a buscar y una lista de tuplas y busca dentro de la lista todas las entradas
    que contienen el el nombre completo la cadena recibida''' 
    cadena = input('Ingrese la cadena a buscar: ')
    listu= ('María: 3743'),('Mauro: 3425'),('Marcos: 52425'),('Fiona: 423324')
    a = list(listu)
    acum = []
    for x in a: 
        if cadena in x: 
            acum.append(x)
    print(acum)

agenda_simplificada()
