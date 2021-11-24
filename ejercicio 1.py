def estadoAgua (temperatura):
    if(temperatura<0):
        print('El estado del agua es hielo')
    elif(temperatura>=0 and temperatura<=100):
        print('El estado del agua es líquido')
    else:
        print('El estado del agua es vapor')
