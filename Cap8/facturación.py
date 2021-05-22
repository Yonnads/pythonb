def facturador():
    ''' El programa cuenta con una lista ordenada de productos, en la que  cada uno consiste en una tupla 
    de (identificador, descripción, precio), y una lista de productos a facturar, en la que cada uno consiste 
    en una tupla de (identificador, cantidad) . 
    Genera una factura que incluye la cantidad, la descripción, el precio unitario, el precio total y al final
    imprime el total general'''

    productos = (('001', 'azucar', 90),('002', 'leche', 80), ('003','café', 200), ('004', 'chocolate', 140))
    facturar = (('001', 21),('002', 525), ('003', 26265), ('004', 1222))
    factura =list()
    total = 0
    for l in facturar: 
        a = l[0]
        print (a)
        for x in productos: 
            if a == x[0]: 
                factura.append(l[1])
                factura.append(x[1])
                factura.append(x[2])
                d = l[1]*x[2]
                factura.append(d)
                total += d
    factura.append(total)

    
                

    print((factura))
#devuelve una cadena horrible. No hace lo solicitado
facturador()