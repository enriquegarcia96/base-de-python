

class Persona:
    nombre = "",
    appaterno = "",
    apmaterno = "",
    edad = ""

    def __init__(self, nombre, appaterno, apmaterno, edad):
        self.nombre = nombre
        self.appaterno = appaterno
        self.apmaterno = apmaterno
        self.edad = edad


    def saludo(self):
        print("Hola como estas ", self.nombre, self.appaterno, self.apmaterno)

    def calcular_edad(self):
        return self.edad + 5

    def calcular_faltante_edad(self):
        return 100 - self.edad

opersona = Persona("Enrique", "García", "Romero", 26)

opersona.saludo()