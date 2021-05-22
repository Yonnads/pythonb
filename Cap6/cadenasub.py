def subcad():
    p1 = input('Ingrese una palabra: ')
    p2 = input('Ingrese otra: ')
    if p2 in p1: 
        print(p2,'es una subcadena de', p1)
    else: 
        print('No es una subcadena')
        
subcad()
