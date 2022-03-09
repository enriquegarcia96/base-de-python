# nombre, apellido paterno, apellido materno, edad

# tu defines la estructura
class Persona:
    nombre = "",
    appaterno = "",
    apmaterno = "",
    edad = 0

    def saludo(self):
        print("Hola como estas :", self.nombre)






#Creamos el objeto
opersona1 = Persona()

#Llenamos la informacion
opersona1.nombre = "Enrique man"
opersona1.appaterno = "García"
opersona1.appaterno = "Romero"
opersona1.edad = 28

print(opersona1.edad)
print(opersona1.appaterno)
opersona1.saludo()





