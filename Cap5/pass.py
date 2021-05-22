#Ejercicio 5.7.3  Manejo de contraseñas
def password(): 
    while True:
        contraseña = input('Ingrese la contraseña: ')
        if contraseña == 'Password': 
            print('Bienvenido')
            break

#Esta parte es la a
password()

def contra(): 
    import time
    n= 0
    for x in range(5): 
         contraseña = input('Ingrese la contraseña: ')
         
         if contraseña != 'Password': 
             n +=5
             time.sleep(n)
             print('Contraseña incorrecta, intentelo nuevamente: ')
             continue
         else:
             print('Contraseña correcta, bienvenido')
             break
             


contra()