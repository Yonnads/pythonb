def maxprod(a,b,c,d):
    #Ejercicio 3.9.3
    """devuelve el mayor producto entre cuatro nros""" 
    multi= (a*b), (a*c), (a*d), (b*c), (b*d), (c*d) 
      
    return max(multi) 

maxprod()