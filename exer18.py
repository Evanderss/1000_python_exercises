# Calcular la suma de tres númneros, incluir la condición de igualdad

def suma_numeros(a: int, b: int, c: int) -> int:
    suma = a + b + c

    if a == b and a == c:
        suma *= 3
    return suma

if __name__ == "__main__":
    print(suma_numeros(2, 2, 7))
    print(suma_numeros(2, 2, 2))