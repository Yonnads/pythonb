def repetidor():
    ''' El programa le pide una palabra al usuario y luego la imprime en una unica lina 1000 veces
    con espacios intermedios 
    '''
    a=input("Por favor ingrese una palabra: ")  
    for b in range(1000):
        print(a, end= ' ')

repetidor()
