def notas():
    #Ejercicio 5.7.1
    ''' El usuario ingresa notas y el programa le pregunta si quiere ingresar más notas
    e imprime el promediocorrespondiente''' 
    n= "si"
    notas = ' '
    while n == "si":
        notas += input('Ingrese su nota: ') + ' '
        n= input('¿Quiere ingresar más notas? <si-no>: ')
        print('Tus notas: ',notas)

notas()