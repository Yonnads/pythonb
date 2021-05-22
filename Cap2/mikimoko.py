def obtener_mikimoko(n):
    '''
    recibe n y devuelve n, mo Miki si es mult de 3, 
    o Moko si es mult. de 5, o MikiMoko sis mult. de 3 y 5
    '''
    if n % 3 == 0 and n%5== 0:
        return 'MikiMoko'
    if n % 3 == 0: 
        return 'Miki'
    if n % 5 == 0: 
        return 'Moko'

    return n



def mikimoko(n):
    '''Imprime entre 1 y n los números mikimoko'''
    for i in range(1, n+1):
        print(obtener_mikimoko(i))

mikimoko(100)
