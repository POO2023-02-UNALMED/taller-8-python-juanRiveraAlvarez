class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, deporte, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, años_practicando)
        self.goles_marcados = goles_marcados
        self.tarjetas_rojas = tarjetas_rojas
        self.pierna_habil = pierna_habil
        Futbolista.listaFutbolistas.append(self)

    def __str__(self):
        persona_info = super(Persona, self).__str__()
        deportista_info = super(Deportista, self).__str__()
        return f"{persona_info} {deportista_info} Tengo {self.goles_marcados} goles marcados, {self.tarjetas_rojas} tarjetas rojas y mi pierna hábil es {self.pierna_habil}."
