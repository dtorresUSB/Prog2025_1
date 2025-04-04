class Futbolista():
    def __init__(self):
        self.dorsal = None
        self.posicion = None
        self.equipo = 'Barcelona'
        self.edad = None
        self.nombre = None

    def setDorsal(self,dorsal:str):
        if '0'<=dorsal<='99':
            self.dorsal = dorsal
            return True
        print('El dorsal debe ser un numero entre 0 y 99\n')
        return False

    def getDorsal(self):
        return self.dorsal
    
    def setPosicion(self,posicion:str):
        self.posicion = posicion.capitalize()
        return True

    def getPosicion(self):
        return self.posicion

    def setEdad(self,edad:str):
        if 16 <= int(edad) <= 42:
            self.edad = edad
            return True
        print('La edad debe ser un numero entre 16 y 42\n')
        return False

    def getEdad(self):
        return self.edad
    
    def setNombre(self,nombre:str):
        self.nombre = nombre.capitalize()
        return True

    def getNombre(self):
        return self.nombre
    
    def getEquipo(self):
        return self.equipo
    
    def presentacion(self):
        return f'Nombre del jugador: {self.getNombre()}\n'\
          f'Edad: {self.getEdad()}\n'\
          f'Equipo: {self.getEquipo()}\n'\
          f'posición: {self.getPosicion()}\n'\
          f'Dorsal: {self.getDorsal()}'