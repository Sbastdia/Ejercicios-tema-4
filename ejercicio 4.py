def añoBisiesto(Año):
    Bisiesto=False
    if(Año%4==0):
        if(Año%100==0):
            if(Año%400==0):
                Bisiesto=True
        else:
            Bisiesto=True
    return Bisiesto

def diaSemana(dia, mes, año):
    cifras=año%100
    cifras+=cifras/4
    cifras+=dia
    if(mes==1):
        cifras+=1
        if(añoBisiesto(año)==True):
            cifras-=1
    elif(mes==2):
        cifras+=4
        if(añoBisiesto(año)==True):
            cifras-=1
    elif(mes==3):
        cifras+=4
    elif(mes==4):
        cifras+=0
    elif(mes==5):
        cifras+=2
    elif(mes==6):
        cifras+=5
    elif(mes==7):
        cifras+=0
    elif(mes==8):
        cifras+=3
    elif(mes==9):
        cifras+=6
    elif(mes==10):
        cifras+=1
    elif(mes==11):
        cifras+=4
    elif(mes==12):
        cifras+=6

    siglo=año/100
    if(siglo==16 or siglo==20):
        cifras+=6
    elif(siglo==17 or siglo==21):
        cifras+=4
    elif(siglo==18):
        cifras+=2
    elif(siglo==19):
        cifras+=0

    modulo=cifras%7
    queDiaEs=''
    if(modulo==1):
        queDiaEs= 'Hoy es domingo'
    elif(modulo==2):
        queDiaEs='Hoy es lunes'
    elif(modulo==3):
        queDiaEs= 'Hoy es martes'
    elif(modulo==4):
        queDiaEs= 'Hoy es miércoles'
    elif(modulo==5):
        queDiaEs= 'Hoy es jueves'
    elif(modulo==6):
        queDiaEs= 'Hoy es viernes'
    elif(modulo==0):
        queDiaEs= 'Hoy es sábado'

    return queDiaEs