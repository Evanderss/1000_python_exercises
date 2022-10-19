# Crear una función únicamente para sumar números enteros
def sumar(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else: 
        raise TypeError("Ingresa un número entero")

if __name__ == "__main__":
    try:
        print(sumar(2, 3 ))
        print(sumar("2", "3"))
    except TypeError as e:
        print(e)