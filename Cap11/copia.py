def cp():
    '''La función copia todo el contenido de un archivo a otro de modo que queda exactamente igual'''
    with open('archivo.txt') as archivo: 
        guardar = ''
        linea = archivo.readline()
        while linea != '': 
            linea = archivo.readline()
            guardar += linea
        with open('vacio.txt', 'w') as vacio:
            vacio.write(guardar)


cp()