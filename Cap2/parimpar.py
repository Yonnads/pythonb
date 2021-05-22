def par_impar():
    #Ejercicio 2.6.6
    'la funcion devuelve 1 si es par o 0 si es impar'
    n = int(input("Ingrese un número entero: "))
    if n % 2 == 0:
        return 1
    else:
        return 0
        
par_impar()

def dig(): 
    a = input('Ingrese un nro entero: ')
    return len(a)
dig()

def pares():
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    for c in range(a, b+1):
        if c % 2 == 0:
            print (c)

pares()

def multiplo10(): 
    numero = (int(input('Ingrese un nro: ')) // 10) * 10
    print(numero)

multiplo10()




