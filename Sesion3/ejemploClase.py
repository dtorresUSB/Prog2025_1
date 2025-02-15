limiteSuperior=10
limiteInferior=0
num= int(input('Ingrese un numero: '))
if num>=limiteInferior:
    #Evalua el True
    if num<=limiteSuperior:
        #Evalua el True
        if num%2==0:
            #Evalua el True
            print('El numero esta en rango y es par')
        else:
            print('El numero esta en rango y es impar')
    else:
        print('El numero es muy alto')
else:
    print('El numero esta muy bajo')
