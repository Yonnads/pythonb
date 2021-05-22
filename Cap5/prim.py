def dicpri():
    #Ejercicio 5.7.10 
    num = int(input("Ingrese un nro: "))
    for n in range(2,num+1): 
        a = n
        for x in range(2,a+1):
            if a % x == 0 and x != a: 
                break
            elif a % x == 0 and x == a:
                print(a)


dicpri()    


