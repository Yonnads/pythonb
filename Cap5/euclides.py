def nroeucli(m,n): 
    #Ejercicio 5.7.5
    '''El programa recibe 2 nros enteros y devuelve el MCD entre ambos'''
    while True: 
        r = m % n
        if r == 0:
            print(n, 'es el MCD')
            break
        else: 
            m = n
            n = r 

nroeucli()