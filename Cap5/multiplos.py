def multiplos(m,n):
    #Ejercicio 5.7.9 a 
    a = 0
    for x in range(m,n): 
        if x % m == 0:
            a +=1 

    print((a)) 

multiplos()

