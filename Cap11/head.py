def head(): 
    '''La función recibe un archivo y un nro N e imprime las primeras N líneas del archivo'''
    a = open(input('Ingrese nombre del archivo: '))
    b = int(input('Ingrese nro de líneas: '))
    linea = a.readlines()
    print(linea[:b]) 

    a.close()
    

    
head()