def elementos(busqueda,elemento):
    '''La funcion recibe una lista ordenada y un elemento. Si el elemento se encuentra en la lista,
    debe encontrar su posición mediante la busqueda binaria y devolverlo. Si no se encuentra, debe agregarlo a 
    la lista en la posición correcta y devolver esa nueva posición'''

    izq = 0
    der = len(busqueda) -1
    while izq <= der: 
        medio = (izq + der) // 2
        if busqueda[medio] == elemento:
            a = busqueda.index(elemento)
            print (f'La posición del elemento es: {a}')
        if busqueda[medio]> elemento: 
            der = medio -1
        else:
            izq = medio + 1
        k = elemento -1  
        if busqueda.index(k) != elemento: 
            busqueda.insert(k,elemento)
            print(f'la posición del elemento es: {busqueda.index(elemento)}')

            break

    print(busqueda)
    #Resuelve el problema pero se podría mejorar ya que el programa exige que haya un nro menor al que se desea agregar 
    #Debería mejorarlo si o si para que evalúe si el ultimo nro menor que el y lo agregue 

elementos()

