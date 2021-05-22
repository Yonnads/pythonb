def agenda():
    diccionario = {'felipe': 342525, 'maria': 6252525, 'tracy': 277272, 'raquel': 77474627828, 'yanine': 8282828}
    while True:
        nombre = (input("Ingrese un nombre o  * para terminar: "))
        if nombre == '*': 
            break
        if nombre in diccionario: 
            return(diccionario[nombre])
            modificación = (input('¿Desea modificarlo? Ingrese si o no: '))
            if modificación == 'si': 
                diccionario.pop(nombre)
                diccionario[nombre] = input('Ingrese el nro nuevo: ')
            else: 
                continue
        else: 
            agregar = input(f'{nombre} no se encuentra en la agenda, ¿desea agregarlo como contacto nuevo? ingrese si o no: ')
            if agregar =='si':
                diccionario[nombre] = input('Ingrese el nro de contacto: ')
    
agenda()

