def rectángulo(): 
	print("Calculo del perímetro y el área de un rectángulo: ")
	base= int(input("Ingrese el número de la base: "))
	altura= int(input ("Ingrese el número de la altura: "))
	perimetro= 2*(base + altura)
	area= (base*altura)
	print("El perímetro del rectángulo es: ",perimetro, "cm")
	print("El área del rectángulo es: ",area, "cm" )

rectángulo()

def círculo():
	print("Calculo del perímetro y área  de un círculo a partir de su radio")
	radio= int(input("Ingrese el número del radio: "))
	areacirculo= 3.14*(radio**2)
	perimcirculo= (2*3.14)*radio
	print("El perímetro del círculo es: ",perimcirculo, "cm")
	print("El área del círculo es: ",areacirculo, "cm")

círculo()

def esfera():
	print("Calculo del volumen de una esfera a partir de su radio")
	radesfera= int(input("Ingrese el número del radio: "))
	esferad= (4/3 *3.14) * (radesfera**3)
	print("El volumen de la esfera es: ",esferad, "cm")

esfera()

def hipotenusa():
	print("Calculo de hipotenusa")
	cateto1= int(input("Ingrese la medida del cateto adyacente: "))
	cateto2= int(input("Ingrese la medida del cateto opuesto: "))
	hipo= (cateto1**2) + (cateto2**2)
	hipot= hipo**.5 
	print("La medida de la hipotenusa es: ", hipot, "cm")

hipotenusa()