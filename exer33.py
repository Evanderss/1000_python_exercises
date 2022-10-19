# Sumar dos números. Si la suma está entre 10 y 30 , retornar 30.
def sumar(x: int, y: int) -> int:
    suma = x + y
    if suma in range (10, 31):
       return 30
    # Otra opción es
    # if suma >= 10 and suma <= 30:
    #    return 30    
    else:
        return suma

if __name__ == "__main__":
    print(sumar(5, 2))
    print(sumar(10, 10))
    