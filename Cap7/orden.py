def tupord(n):
    ''' La funcion recibe una tupla de elementos e indica si están ordenados o no'''
    a = tuple(n)

    if a == tuple(sorted(a)):
        print('Están ordenados')
    else:
        print('No están ordenados')

tupord()