from Futbolista import Futbolista



def imprimirJugadores():
    n=0
    for plantilla in club:
        n+=1
        print(f'--------Jugador{n}--------')
        print(plantilla.presentacion(),'\n')

def imprimirNombres():
    n=0
    for plantilla in club:
        n+=1
        print(f'{n}. {plantilla.getNombre()}')

def ingresarJugador():
    jugador = Futbolista()
    param = ['el dorsal','la posicion','la edad','el nombre']
    info =[jugador.setDorsal,jugador.setPosicion,jugador.setEdad,jugador.setNombre]

    for i in range(4):
        txt = f'Ingrese {param[i]}: ' 
        campo = input(txt)
        respuesta = info[i](campo)

        if not respuesta:
            return
    
    print('Ingreso Exitoso')
    club.append(jugador)

def modificarDatos():
    print('Seleccione uno de los siguientes jugadores: ')
    imprimirNombres()
    opc1 = int(input('Seleccione el numero de un jugador: '))

    jugador = club[opc1-1]

    print('Que información desea modificar: \n'
          '1.Nombre\n'
          '2.Dorsal\n'
          '3.Posición\n'
          '4.Edad\n')
    opc2 = int(input('Seleccione una de las anteriores opciones: '))

    info =['s',jugador.setNombre,jugador.setDorsal,jugador.setPosicion,jugador.setEdad]

    modificacion = input('Ingrese la modificiación de: ')
    info[opc2](modificacion)
      
def menu():
    print('Bienvenido al sistema de registro de los jugadores del '
    'Barcelona\n'
    f'1. Ingresa un nuevo jugador\n'
    f'2. Modificar datos de un jugador\n'
    f'3. Listar los jugadores del club\n')
    opc=int(input('Escoja una de las anteriores opciones: '))

    fcn = ['s',ingresarJugador,modificarDatos,imprimirJugadores]

    jugador = fcn[opc]()
    

def main():
    while 1:
        menu()

club = []  
if __name__ == "__main__":
    main()
    