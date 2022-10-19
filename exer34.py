# Validar dos números. Si son iguales o la suma o el valor absoluto son 5

def validar_numeros(x: int, y: int) -> bool:
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False

if __name__ == "__main__":
    print(validar_numeros(3, 3))
    print(validar_numeros(5, 7))
    