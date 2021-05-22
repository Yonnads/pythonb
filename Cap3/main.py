import saludos

def main():
    nombre = input("¿Cuál es tu nombre?: ")
    print(saludos.hola(nombre))
    print(saludos.adios(nombre))

main()