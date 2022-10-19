# Calcular la suma de tres números diferentes, si son iguales la suma será 0

def sumar(x: int, y: int, z: int) -> int:
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z

if __name__ == "__main__":
    print(sumar(2, 5, 3))
    print(sumar(5, 5, 5))