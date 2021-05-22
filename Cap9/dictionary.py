def tuplas_a_diccionario(l):
    '''la función recibe una lista de tuplas, y devuelve un diccionario
    donde las claves son los primeros elementos de las tuplas, y los valores una lista con los segundos'''
    return dict(l)

def diccionario(): 
    l = [('hola', 'don pepito'), ('hola', 'don josé'),('buenos', 'días')]
    print(tuplas_a_diccionario(l))

diccionario()
