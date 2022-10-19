# Calcular la distancia entre dos puntos cartesianos
from math import sqrt
from re import X

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcular_distancia(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

if __name__ == "__main__":
    punto1 = Punto(3, 2)
    punto2 = Punto(-3, -5)
    print(calcular_distancia(punto1, punto2))