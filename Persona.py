class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_altura(self):
        return self.altura

    def get_sexo(self):
        return self.sexo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_altura(self, altura):
        self.altura = altura

    def set_sexo(self, sexo):
        self.sexo = sexo
