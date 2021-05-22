def factor():
    #Ejercicio 2.6.9 
    ''' La toma una cantidad m de valores ingresados por el usuario, a cada uno le calcula el factorial 
    y luego imprime el resultado junto con su nro de orden'''
    import math
    m = int(input('Ingrese un nro entero: '))
    for x in range(1, m +1):
        a = math.factorial(x)
        print(x, a, sep='-')

factor()

