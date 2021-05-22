import random

CANT_DIGITOS =5

def mastermind(): 
    '''Función principal del juego mastermind''' 
    print('Bienvenido al Mastermind!')
    print(f'tienes que adivinar un número {CANT_DIGITOS} cifras distintas ')

    codigo = elegir_codigo()
    intentos = 1 
    propuesta = input('Qué código propones?: ')
    ME_DOY = 'Me doy'

    while propuesta != codigo and propuesta != ME_DOY:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print(f'Tu propuesta ({propuesta}) tiene {aciertos} aciertos y {coincidencias} coincidencias.')
        propuesta = input('Propone otro código: ')

    if propuesta == ME_DOY: 
        print(f'Mala suerte! El código era:{codigo}')
    else:
        print(f'Felicitaciones! Adivinaste el código en {intentos}')

def elegir_codigo(): 
    '''Devuelve el código de CANT_DIGITOS, dígitos elegidos al azar'''
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ''
    for i in range (CANT_DIGITOS): 
        candidato = random.choice(digitos)
        #Debemos asegurarnos de no repetir digitos
        while candidato in codigo: 
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo

def analizar_propuesta(propuesta, codigo): 
    '''Determina la cantidad de aciertos y coincidencias'''
    aciertos = 0
    coincidencias = 0 
    for i in range(CANT_DIGITOS): 
        if propuesta[i] == codigo [i]: 
            aciertos = aciertos + 1
        elif propuesta [i] in codigo: 
            coincidencias = coincidencias + 1
    return aciertos, coincidencias

mastermind()


    