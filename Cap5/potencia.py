def poten(n):
    #Ejerccicio 5.7.6 a
    '''La función recibe por parámetro un nro y devuelve True si el nro es una potencia de 2 o false en caso contraio'''
    import math
    a = int(math.log(n,2))
    h = 2 ** a
    if h == n : 
        return  True
    else:
        return  False






def potence():
    #Ejercicio 5.7.6 b
    n1 = int(input('Ingrese un nro: '))
    num2 = int(input('Ingrese un nro: '))
    potencias = 0
    for x in range(n1, num2+1):
        c = poten(x)
        if c == True:
            y = (x)
            potencias += y 
        else:
            potencias += 0
    print(potencias)

potence()


            

