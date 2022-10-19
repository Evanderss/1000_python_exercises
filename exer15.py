# Calcular el volumen de una esferada dado su radio

from math import pi

r = float(input("Ingresa el radio de la esfera: "))
volumen = (4/3 * pi * r**3)
print(f"el volumen de la esfera es {volumen} unidades cubicas")