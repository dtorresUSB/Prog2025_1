class Futbolista():
    def __init__(self):
        self.dorsal = None
        self.posicion = None
        self.equipo = None
        self.edad = None
        self.nombre = None
    
    def anotarGol(self):
        return 'GOOOOOOOOL!'

def main():
    jugador1 = Futbolista()
    jugador1.nombre = 'Radamel Falcao Garcia'
    jugador1.edad = 36
    jugador1.equipo = 'Millonarios'
    jugador1.posicion = 'Delantero'
    jugador1.dorsal = 9
    print(id(jugador1))

    print(f'Nombre del jugador: {jugador1.nombre}\n'
          f'Edad: {jugador1.edad}\n'
          f'Equipo: {jugador1.equipo}\n'
          f'posición: {jugador1.posicion}\n'
          f'Dorsal: {jugador1.dorsal}')
    print(jugador1.anotarGol()+'\n')

    jugador2 = Futbolista()
    jugador2.nombre = 'James David Rodriguez'
    jugador2.edad = 33
    jugador2.equipo = 'Leon'
    jugador2.posicion = 'Medio Campista'
    jugador2.dorsal = 10
    print(id(jugador2))

    print(f'Nombre del jugador: {jugador2.nombre}\n'
          f'Edad: {jugador2.edad}\n'
          f'Equipo: {jugador2.equipo}\n'
          f'posición: {jugador2.posicion}\n'
          f'Dorsal: {jugador2.dorsal}')
    print(jugador2.anotarGol()+'\n')

if __name__ == "__main__":
    main()

#variables:  esPrimo        es_primo
#clases:     Persona(), Frutas()    PersonaNatural(),PersonaJuridica()
#funciones:  esPrimo()      es_primo()
#campos:     self.numero    self.esNumero
#metodos:    anotarGoles(), numeroIdentificacion()
