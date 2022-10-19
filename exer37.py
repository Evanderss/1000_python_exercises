# Crear una jerarquía de herencia básica 
class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
    
class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera

if __name__ == "__main__":
    student = Estudiante("INE", "German", "ger@gmail.com", "987", "Ing. computacional")
    print(isinstance(student, Estudiante))
    print(isinstance(student, Persona))