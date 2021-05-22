def adivinador():
    #Ejercicio 5.7.4
    import random
    a = int(random.randrange(1000))
    while True: 
        num = int(input('Ingrese un nro: '))
        if num > a:
            print('Es un nro menor')
        elif num < a: 
            print('Es un nro mayor')
        else: 
            print(num,'es correcto')
            break

adivinador()