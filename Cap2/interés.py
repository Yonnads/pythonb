#Ejercicio 2.6.2
def interés():
    return (100*((1+12/100)**3))

interés()

def cuenta():
    c= float(input("Ingrese la cantidad de pesos inicial: "))
    x= float(input("Ingrese el monto de la tasa de interés: "))
    n= float(input("Ingrese el número de años: "))
    print("El monto final a obtener es: ",(c*((1+x/100)**n)))

cuenta()