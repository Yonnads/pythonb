def maximin(m,r1,r2): 
    while True: 
        nro = int(input(m))
        if nro <= r1:
            continue
        elif nro >= r2: 
            continue
        else: 
            print(nro)
            break

maximin()
    

