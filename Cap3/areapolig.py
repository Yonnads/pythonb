def arpoligono(x,y,z):
    #Ejercicio 3.9.4 a
    """ La función recibe coordenadas de un vector (x, y, z) y devuelve su norma """
    import math 
    N = math.sqrt(x*x + y*y + z*z)
    return N

def vecdif(x1, y1,z1,x2,y2,z2):
    #Ejercicio 3.9.4 b
    """La función recibe las coordenadas de dos vectores R3 y devuelve las coordenadas de del vector diferencia"""
    return (x1-x2), (y1-y2), (z1-z2)


def prodvec(x1,y1,z1,x2,y2,z2):
    #Ejercicio 3.9.4 c
    return (y1*z2-z1*y2), (z1*x2-x1*z2), (x1*y2-y1*x2)

def areatri(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    #Ejercicio 3.9.4 d
    p1= vecdif(x1,y1,z1,x2,y2,z2) #Toma las coord de los vectores AyB, y devuelve las coord del vec diferencia
    r1,r2,r3 = p1 #Desempaqueta las coord del vector AB
    v1= vecdif(x1,y1,z1,x3,y3,z3) #Toma las coord de los vectores AyC, y devuelve las coord del vec diferencia
    g1,g2,g3 = v1 #Desempaqueta las coord del vector AC
    h1= prodvec(r1,r2,r3,g1,g2,g3) #Calcula el producto vectorial AB * AC
    w1,w2,w3 = h1 #Desempaqueta las coord del prod vectorial
    ñ1 = arpoligono(w1,w2,w3) # Toma las coord antes obtenidas y devuelve su norma
    c1 = ñ1 / 2 # Divide a la mitad la norma, obteniendose el area del triangulo

    return "El area del triángulo es: ", c1 #Devuelve el area del trangulo

areatri()






