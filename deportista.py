class Deportista:
    def __init__(self, deporte="Fútbol", añosPracticando=0):
        self.deporte = deporte
        self.añosPracticando = añosPracticando

    def getDeporte(self):
        return self.deporte

    def getAñosPracticando(self):
        return self.añosPracticando

    def setDeporte(self, deporte):
        self.deporte = deporte

    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando
