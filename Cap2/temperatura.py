def conversor():
    #ejercicio 2.6.4
    """Convierte la temperatura de grados Farenheit a Celcius"""
    f = (float(input("Ingrese la cantidad en grados Farenheit: "))-32)*5/9
    print("El equivalente en grados celcius es: ", f)

conversor()

def conver():
    #Ejercicio 2.6.5 
    for x in range(0,121,10):
        c = (x-32)*5/9
        print (f"El valor en grados farenheit es: {x} -  Su equivalente en grados celsius es: {c}")

conver()

