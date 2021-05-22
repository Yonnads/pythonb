def main():
    """El usuario ingresa la tarifa por segundos, la cantidad de comunicaciones realizadas, 
    y la duración de cada comunicación expresada en horas, minutos y segundos. Como resultado
    se informa la duración en segundos de cada comunicación y su costo""" 

    p = float(input("¿Cuánto cuesta 1 segundo de comunicación?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántas minutos?: "))
        s = int(input("Cuántos segundos?: "))
        duración = a_segundos(h,m,s)
        costo = duración * p
        print("Duración:",duración,  "Segundos . Costo: $", costo)

def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo, expresada en
    horas, minutos, y segundos """
    return 3600 * horas + 60 * minutos + segundos

main()