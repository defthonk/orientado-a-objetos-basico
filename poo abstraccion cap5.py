# Clases abstractas 
# - No las vamos a instanciar nunca directamente 
# - Contiene por lo menosun metodo abstracto 
# - Las vamos a usar de base para subclase mas especifica 

# Metodos abstractos 
# - Debemos sobreescribirlos en cada una de las subclases

from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod #Decorador, osea lo que  hago es convertir un metodo, en un metodo abstracto
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    def subirDeNivel(self):
        self.nivel += 1
        
    def verInventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Pocion de mana", "Grimorio"]

    def getStatus(self):
        print(f"clase mago")
        super().getStatus()


    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia*0.6
        print(f"Vida actual del objetvido es: {objetivo.vida}")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75 
        self.inventario = ["Pocion de vida", "Escudo", "Espada"]
    
    def getStatus(self):
        print(f"clase guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f" el objetivo se ha quedado con {objetivo.vida} puntos de vida ")

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")

guerrero.getStatus()
mago.getStatus()

mago.verInventario()
guerrero.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)
