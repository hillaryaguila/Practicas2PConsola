class Persona:
    def __init__(self, nombre, edad, anioNacimiento, anioActual):
        self.nombre = nombre
        self.edad = edad
        self.anioNacimiento = anioNacimiento
        self.anioActual = anioActual

    def __str__(self):
        return f"Persona(edad={self.anioActual - self.anioNacimiento})"

         