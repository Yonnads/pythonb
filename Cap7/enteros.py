def maymen():
    enteros = list(input('Ingrese los enteros: '))
    com = (input('Ingrese un nro entero: '))
    menores = []
    iguales = []
    mayores = []
    for m in enteros:
        if m < com:
            menores.append(m)
        elif m == com: 
            iguales.append(m)
        else: 
            mayores.append(m)
    print(f'Los menores son: {menores}, los iguales son: {iguales}, los mayores son: {mayores}')

maymen()