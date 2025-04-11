class Animal:
    def __init__(self,nombre,color,raza):
        self.nombre = nombre
        self.color = color
        self.raza = raza
    
    #-----------Setters---------
    def setNombre(self,nombre:str):
        self.nombre = nombre

    def setColor(self,color:str):
        self.color = color

    def setRaza(self,raza:str):
        self.raza = raza
    #------------Getters--------
    def getNombre(self):
        return self.nombre 

    def getColor(self):
        return self.color 

    def getRaza(self):
        return self.raza 
    
    #-----------Metodos----------
    def hacerSonido(self):
        return 'piuu piuuu'
    
    def comer(self):
        return 'me gusta comer alpiste'

class Perro(Animal):
    def __init__(self,nombre,color,raza,hora):
        super().__init__(nombre,color,raza)
        self.horaSalida = hora

    def setHoraSalida(self,hora:str):
        self.horaSalida = hora

    def getHoraSalida(self):
        return self.horaSalida
    
     #-----------Metodos----------
    def hacerSonido(self):
        return 'Wouffffff'
    
class Gato(Animal):
    def __init__(self,nombre,color,raza,vidas):
        super().__init__(nombre,color,raza)
        self.numeroVidas = vidas
    
    def setNumeroVidas(self,vidas:int):
        self.numeroVidas = vidas

    def getNumeroVidas(self):
        return self.numeroVidas
    
     #-----------Metodos----------
    def hacerSonido(self):
        return 'Miiiiiiiauuuuuu'
    
    def comer(self):
        return 'me gusta comer lasagna'


    