def segundero(h,m,s): 
    #Ejercicio 3.9.1 a
    """ Calcula la duración en segundos de un intervalo dado en horas, minutos y segundos"""
    return (3600*h + 60*m + s)



def hms(s): 
    #Ejercicio 3.9.1 b
    """ Calcula la duración en horas, minutos y segundos de un intervalo dado en segundos """
    h = s//3600
    m = (s % 3600) // 60 
    segundo = (s % 3600) % 60 
    return(h, m,segundo)
 

def sumasegundos(): 
    #Ejercicio 3.9.2
    """ Calcula la suma en segundos dos intervalos de tiempos en horas, minutos y segundos, ingresados por el usuario"""
    acumulado = 0
    for x in range(2): 
        o = int(input("Cuantas horas?: "))
        i = int(input("Cuantos minutos?: "))
        e = int(input("Cuantos segundos?: "))
        acumulado += segundero(o,i,e)

    b = hms(acumulado)
  
    print (b)
        

sumasegundos()
