porcentaje = int(input('Ingrese el porcentaje de zurdos que desea dentro la sala: '))
personas = 100/(100-porcentaje)
#print('La cantidad de zurdos que debe sacar de la sala es ', personas)
print('debe sacar '+ str(personas) + 
      ' zurdos de la sala para que el porcentaje sea igual a ' + 
      str(porcentaje) + '%')