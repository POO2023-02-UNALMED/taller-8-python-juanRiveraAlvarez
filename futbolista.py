
from deportista import Deportista
from persona import Persona
class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo,añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Fútbol", añosPracticando)
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.golesMarcados
    
    def getTarjetasRojas(self):
        return self.tarjetasRojas
    
    def getPiernaHabil(self):
        return self.piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte Futbol Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"