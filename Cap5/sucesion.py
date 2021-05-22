def sucesion():
    suma= 0 
    acumulado= []
    while True: 
        centinela = (input("Ingrese un nro entero o  -1 para terminar: "))
        if centinela == '-1': 
            break
        x = int(centinela)
        suma += x
        acumulado.append(x)
    a = len(acumulado)
    promedio = suma / a
    print(f'la cantidad de nros ingresados es {a}, su suma es: {suma}, y su promedio: {promedio}')

sucesion()

