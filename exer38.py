# Resolver la expresión algebraica (x + y) * (x + y)
def evaluar_expresion(x: float, y: float) -> float:
    return x**2 + 2*x*y + y**2

if __name__ == "__main__":
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    print(evaluar_expresion(x, y))