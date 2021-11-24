def categoriaDeportiva(edad):
    if(edad<6):
        print('Aún es pronto para estar en una categoría')
    elif(edad>=6 and edad<=7):
        print('Categoría: benjamín')
    elif(edad>=8 and edad<=9):
        print('Categoría: alevín')
    elif(edad>=10 and edad<=11):
        print('Categoría: infantil')
    elif(edad>=12):
        print('Categoría: cadete')