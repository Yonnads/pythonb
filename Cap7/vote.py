def vote():
    '''La funcion recibe una tupla con nombres y para cada uno imprime un mensaje'''
    nombre = ('Anna', 'Kevin', 'Tina')
    for x in nombre: 
        print(f'Estimado {x}, vote por mi')

vote()
def vote2():
    '''La funcion recibe una tupla con nombres, una posición de origen
y una cantidad e imprime el mensaje para los n nombres a partir de la posicion'''
    n = 5
    p = 2
    name = ('Anna', 'Kevin', 'Tina', 'Felipe', 'Robert', 'Demian')
    for l in name[p:n]: 
        print(f'Estimado {l}, vote por mi')

vote2()