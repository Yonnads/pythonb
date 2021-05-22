def operaciones_basicas():
    print("Se obtendrán los resultados de las operaciones básicas entre dos números")

    n1= int(input("Ingrese un número: "))
    n2= int(input("Ingrese otro número: "))
    
    print("La suma es:",(n1+n2))
    print("La resta es:",(n1-n2))
    print("La multipliciación es:", (n1*n2))
    print("La división es:", (n1/n2))

operaciones_basicas()




def tabla_multiplicar():
    "Imprime la tabla de multiplicar"
    numero= int(input("Ingrese un número: "))
    for indice in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"{numero}*{indice} = {numero * indice}")

tabla_multiplicar()