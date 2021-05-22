def repite_hola():
    """
    La función recibe un número y concatena Hola esa cantidad de veces
    """
    n =(int(input("Ingrese el número de veces que quiere repetir hola: ")))
    return "Hola "* n

repite_hola()

def repite():
    """
    La función recibe un número y lo repite Hola esa cantidad de veces
    """
    n =(int(input("Ingrese el número de veces que quiere repetir hola: ")))
    for x in range (1, n+1):
        x = "Hola"
        print (x)

repite()


def rep():
    """
    La función recibe un número y una cadena de texto,
    la cual es repetida esa cantidad de veces
    """
    a = input("Ingrese una cadena de texto: ")
    n =(int(input("Ingrese el número de veces que quiere repetirla: ")))
  
    for x in range (1, n+1):
        x = a
        print (x)

rep()


def re():
    """
    La función recibe un número y concatena Hola esa cantidad de veces
    """
    a = input("Ingrese una cadena de texto: ")
    b = a + " "
    n =(int(input("Ingrese el número de veces que quiere concatenarla: ")))
    return b * n

re()