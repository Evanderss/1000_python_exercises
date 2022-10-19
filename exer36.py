# Crear una clase para representar los datos de una persona 

class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Edad: {self.edad}
        Correo: {self.correo}"""

if __name__ == "__main__":
    persona = Persona("edward", "25", "edward@gamil.com" )
    print(persona)