def consonantes():
    cadena = input('Ingrese el texto: ')
    vocales = 'AÁaáEÉeéIiíOÓoóUÚuúü'
    con =''
    for x in cadena: 
        if x in vocales:
            continue
        else:
            con += x
    print (con)

consonantes()

def vocal():
    texto = input('Ingrese el texto: ')
    voc = 'AÁaáEÉeéIiíOÓoóUÚuúü'
    acuvo = ''
    for x in texto: 
        if x in voc:
            acuvo += x
        
    print (acuvo)

vocal()

def cambiavocal():
    texto = input('Ingrese el texto: ')
    np = ''
    for x in texto:
        if x in ('AÁaá'): 
            np += 'e'
            continue
        if x in ('EÉeé'): 
            np += 'i'
            continue
        if x in ('IÍií'): 
            np += 'o'
            continue
        if x in ('OÓoó'): 
            np += 'u'
            continue
        if x in ('UÚuü'): 
            np += 'a'
            continue
        else: 
            np += x
    print(np)

cambiavocal()

def palindromo(): 
    palabra = input('Ingrese una palabra o frase: ')
    b = palabra[::-1]
    if palabra == b: 
        print('Es un palindromo')
    else:
        print('No es un palindromo')

#Esta funcion hace lo solicitado sin los espacios, cuando hay espacios los lee.

palindromo()