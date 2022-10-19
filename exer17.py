# Crear una función para determinar si un número es cercano a 1000 o 2000

def cercano(n: int) -> int:
    return (abs(1000 - n) < 100) or (abs(2000 - n) < 100)

if __name__ == "__main__":
    print(cercano(1000))
    print(cercano(200))
    print()
    print(cercano(2000))
    print(cercano(3200))