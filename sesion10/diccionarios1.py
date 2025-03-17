estudiantes = {'nombres':['Mateo','Juan','Alfredo','David'],
               'codigo':[1213456,154874,8756844,2145459]}
#print(estudiantes['nombres'])

for i in range (len(estudiantes['nombres'])):
    print(f'{estudiantes['nombres'][i]} es estudiante con codigo',
          f'{estudiantes['codigo'][i]}')