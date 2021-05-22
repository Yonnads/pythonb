#Ejercicio 2.6.1
def ciclos():
    for x in range(10, 21):
        print (x)

ciclos()

def amigos():
    for x in["Daiana", "Carolina", "Jennifer", "Fabixia", "Florencia"]:
        print ("Hola "+ x)

amigos()


def saludos():
    ''' el programa pregunta los nombres de sus seis mejores amigos y los saluda'''
    for x in range(1,7):
	    uno= input("Ingrese el nombre de su amigo: ")
	    print(x,"Hola", uno, "cómo estás amigo? ")

saludos()

def saludos_():
    print ("Salude a sus mejores amigos")
    a= int(input("A cuántos amigos desea saludar: "))
    for x in range(a):
	    uno= input("Ingrese el nombre de su amigo: ")
	    print(x,"Hola", uno, "cómo estás amigo? ")

saludos_()



