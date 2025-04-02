class Futbolista():
    def __init__(self,dorsal,posicion,edad,nombre):
        self.dorsal = dorsal
        self.posicion = posicion
        self.equipo = 'Barcelona'
        self.edad = edad
        self.nombre = nombre

    def presentacion(self):
        return f'Nombre del jugador: {self.nombre}\n'\
          f'Edad: {self.edad}\n'\
          f'Equipo: {self.equipo}\n'\
          f'posición: {self.posicion}\n'\
          f'Dorsal: {self.dorsal}'

def main():
    club = []
    for i in range(3):
        print(f'--------Jugador{i+1}--------')
        dorsal = input('Ingrese el dorsal: ')
        posicion = input('Ingrese la posicion: ')
        edad = input('Ingrese la edad: ')
        nombre = input('Ingrese el nombre: ')
        jugador = Futbolista(int(dorsal),posicion,int(edad),nombre)
        club.append(jugador)
        print('¡Ingreso exitoso de datos!\n')

    print(club)

    n=0
    for plantilla in club:
        n+=1
        print(f'--------Jugador{n}--------')
        print(plantilla.presentacion(),'\n')
    

if __name__ == "__main__":
    main()