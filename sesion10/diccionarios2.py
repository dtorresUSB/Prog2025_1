
def impresion(diccionario, programa):
    for i in range(len(diccionario['nombres'])):
        if diccionario['genero'][i]==1:
            txt='El'
        else:
            txt ='La'
        print(f'{txt} estudiante {diccionario['nombres'][i]} '+
               f'tiene codigo {diccionario['codigos'][i]} ' + 
               f'y es del programa {programa}')
        
def historial(universidad):
    for i in universidad:
        impresion(universidad[i],i)

universidad = {'mecatronica':{'nombres':['Mateo','Juan','Alfredo','David'],
                              'codigos':[1213456,154874,8756844,2145459],
                              'genero':[1,1,1,1]},
               'sonido':{'nombres':['Paula','Roberto','Maria'],
                              'codigos':[551124,784845,145745],
                              'genero':[0,1,0]}}

print('Bienvenido al sistema de registro academico de la universidad de San Buenaventura\n' +
      '1. Historial de estudiantes de Mecatrónica\n' +
      '2. Historial de estudiantes de Sonido\n'+
      '3. Historial de todos los estudiantes')
opc = input('Seleccione una de las siguientes opciones: ')

if opc == '1':
    impresion(universidad['mecatronica'],list(universidad.keys())[0])
elif opc == '2':
    impresion(universidad['sonido'],list(universidad.keys())[1])
elif opc == '3':
    historial(universidad)
 