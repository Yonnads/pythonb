def dados(): 
    '''El programa elige dos números aleatorios entre el 1 y el 6.
    los imprime en pantalla, imprime su suma y le pregunta al usuario si quiere tirar los dados otra vez.'''
    print('Bienvenido al simulador de dados')
    import random 
    inicio = 'SI'
    digitos = 1,2,3,4,5,6
    while True: 
        if inicio != 'SI': 
            break
        n1 = random.choice(digitos)
        n2 = random.choice(digitos)
        print('Los numeros de sus dados son:',n1,'-',n2)
        print('La suma de los mismos es:',n1+n2)
        inicio = (input('¿Quiere tirar los dados otra vez? (ingrese SI o NO): '))

dados()
