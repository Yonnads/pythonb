def main():
    acumulado = 0 
    for i in range(10):
        acumulado += int(input("Ingrese un nro: "))
        print("El acumulado es: ", acumulado)

main()

def mostrar_coords(columnas, filas):
    ''' Imprime todas las coordenadas cartesianas de una 
    matriz de la cant de cols y filas dadas'''
    for f in range(filas):
        for c in range(columnas): 
            print(f, c, sep=',', end= ' ')
        print()

mostrar_coords(3, 4)
